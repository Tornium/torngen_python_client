import typing


class Parameter:
    def __init__(
        self,
        parameter_name: str,
        parameter_in: typing.Literal["query", "path"],
        required: bool,
        deprecated: bool,
    ):
        pass
