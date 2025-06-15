import typing

from RequestLinks import RequestLinks

from ..base_schema import BaseSchema


class RequestMetadataWithLinksAndTotal(BaseSchema):

    total: int
    links: RequestLinks
