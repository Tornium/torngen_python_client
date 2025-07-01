import typing

from base_path import Path


class BaseQuery(object):
    def __init__(self) -> typing.Self:
        self.selections: typing.List[Path] = set()
        self.parameters: typing.Dict[str, typing.Any] = {}
        self.api_key = None

    def select(self, *args: typing.Tuple[Path]) -> typing.Self:
        # By default, Python includes a None value at the end of the args
        args = tuple(arg for arg in args if arg is not None)
        print(args)
        print(list(isinstance(path, Path) for path in args))

        if any(not self.__validate_path(path) for path in args):
            raise TypeError("At least one path is not of type Path")

        self.selections.update(args)
        return self

    def key(self, api_key: str) -> typing.Self:
        self.api_key = api_key
        return self

    def get(self, adapter=None) -> typing.Self:
        # TODO: Implement this
        return self

    def parse(self):
        return NotImplemented

    def __getattr__(self, parameter_name) -> typing.Callable[typing.Any, typing.Self]:
        def setter_method(value: typing.Any) -> typing.Any:
            if not self.__validate_parameter(parameter_name, value):
                raise ValueError(f"Invalid parameter {parameter_name} for the provided paths")

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

