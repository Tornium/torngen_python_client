import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_crime import FactionCrime
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class UserOrganizedCrimesResponse(BaseSchema):
    """
    JSON object of `UserOrganizedCrimesResponse`.
    """

    organizedcrimes: typing.List[FactionCrime]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return UserOrganizedCrimesResponse(
            organizedcrimes=BaseSchema.parse(
                data.get("organizedcrimes"), typing.List[FactionCrime]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
