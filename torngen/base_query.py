import re
import typing
import urllib.parse

from adapter import HTTPAdapter
from base_path import Path
from base_schema import BaseSchema

VERSION = "2.0.0"


class _URLComponents(typing.NamedTuple):
    """
    The parts of the URL used by urllib encode into a string.

    Source: https://docs.python.org/3/library/urllib.parse.html
    Source: https://stackoverflow.com/a/15799706
    """

    scheme: str
    netloc: str
    path: str
    params: str
    query: str
    fragment: str


class BaseQuery(object):
    def __init__(self, base_path: str) -> typing.Self:
        self.base_path: str = base_path
        self.selections: typing.Set[Path] = set()
        self.parameters: typing.Dict[str, str | int] = {}
        self.api_key: typing.Optional[str] = None
        self.response: typing.Optional[dict] = None

    def select(self, *args: typing.Tuple[Path]) -> typing.Self:
        if any(not self.__validate_path(path) for path in args):
            raise TypeError("At least one path is not of type Path")

        self.selections.update(args)
        return self

    def key(self, api_key: str) -> typing.Self:
        if not isinstance(api_key, str):
            raise TypeError("API key must be a string")
        elif len(api_key) != 16:
            raise ValueError("API key must be 16 characters long")
        elif not api_key.isalnum():
            raise ValueError("API key must be alpha-numeric")

        self.api_key = api_key
        return self

    def get(
        self, adapter: typing.Type[HTTPAdapter], new_headers: typing.Dict[str, str] = {}
    ) -> typing.Self:
        headers = {
            "User-Agent": f"{adapter.client_name()} ({adapter.version()}) torngen/{VERSION}",
            "Content-Type": "application/json",
            "Authorization": f"ApiKey {self.api_key}",
        }
        headers.update(new_headers)

        self.response = adapter.get(url=self.url(), headers=headers)
        return self

    def url(self, domain: str = "api.torn.com") -> str:
        path = f"/v2/{self.base_path}/"

        if self.api_key is None:
            raise ValueError("An API key is required")

        for path_parameter, path_parameter_value in self.__path_parameters().items():
            path = path.replace("{" + path_parameter + "}", str(path_parameter_value))

        # The parameters have already been validate by __validate_parameter when they were set so
        # they will not be validated now.
        query_params = {
            "selections": ",".join(
                selection.selection for selection in self.selections
            ),
            **self.__query_parameters(),
        }

        url = urllib.parse.urlunparse(
            _URLComponents(
                scheme="https",
                netloc=domain,
                path=path,
                params="",
                query=urllib.parse.urlencode(query_params).replace("%2C", ","),
                fragment="",
            )
        )

        missing_path_parameter = re.search(r".*\/{(.*)}.*", url)
        if missing_path_parameter:
            raise RuntimeError(f"Missing path parameter {missing_path_parameter.group(1)}")

        # TODO: Required parameters
        # TODO: Warn on deprecated parameters

        return url

    def parse(self) -> typing.Dict[str, BaseSchema]:
        if self.response is None:
            raise ValueError("No API response has been stored")

        parsed_response: typing.Dict[str, BaseSchema] = {}

        selection: Path
        for selection in self.selections:
            parsed_response[selection.selection] = selection.response_schema.parse(
                self.response
            )

        return parsed_response

    def __getattr__(
        self, parameter_name: str
    ) -> typing.Callable[typing.Any, typing.Self]:
        def setter_method(value: str | int) -> typing.Self:
            if not self.__validate_parameter(parameter_name, value):
                raise ValueError(
                    f"Invalid parameter {parameter_name} for the provided paths"
                )

            self.parameters[parameter_name] = value
            return self

        return setter_method

    def __validate_parameter(
        self, parameter_name: str, parameter_value: typing.Any
    ) -> bool:
        path: Path
        for path_name, path in self.__class__.__dict__.items():
            if path_name.startswith("__"):
                continue
            elif not isinstance(path, Path):
                continue
            elif parameter_name not in path.parameters:
                continue

            return True

        return False

    def __validate_path(self, value: Path | typing.Any) -> bool:
        if not isinstance(value, Path):
            return False

        for path_name, path in self.__class__.__dict__.items():
            if value == path:
                return True

        return False

    def __path_parameters(self) -> typing.Dict[str, str | int]:
        valid_path_parameters = set()

        path: Path
        for path_name, path in self.__class__.__dict__.items():
            if path_name.startswith("__"):
                continue
            elif not isinstance(path, Path):
                continue

            valid_path_parameters.update(
                [
                    parameter_name
                    for parameter_name, parameter in path.parameters.items()
                    if parameter.parameter_in == "path"
                ]
            )

        return {
            parameter_name: parameter_value
            for parameter_name, parameter_value in self.parameters.items()
            if parameter_name in valid_path_parameters
        }

    def __query_parameters(self) -> typing.Dict[str, str | int]:
        valid_query_parameters = set()

        path: Path
        for path_name, path in self.__class__.__dict__.items():
            if path_name.startswith("__"):
                continue
            elif not isinstance(path, Path):
                continue

            valid_query_parameters.update(
                [
                    parameter_name
                    for parameter_name, parameter in path.parameters.items()
                    if parameter.parameter_in == "query"
                ]
            )

        return {
            parameter_name: parameter_value
            for parameter_name, parameter_value in self.parameters.items()
            if parameter_name in valid_query_parameters
        }
