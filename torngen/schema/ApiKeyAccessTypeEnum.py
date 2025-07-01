from ..base_schema import BaseSchema


class ApiKeyAccessTypeEnum(BaseSchema):

    values = [
        "Custom",
        "Public Only",
        "Minimal Access",
        "Limited Access",
        "Full Access",
    ]
