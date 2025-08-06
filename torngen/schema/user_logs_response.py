import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links import RequestMetadataWithLinks
from .user_log import UserLog


@dataclass
class UserLogsResponse(BaseSchema):
    """
    JSON object of `UserLogsResponse`.
    """

    log: typing.List[UserLog]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return UserLogsResponse(
            log=BaseSchema.parse(data.get("log"), typing.List[UserLog]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
