import typing

from RequestLinks import RequestLinks

from ..base_schema import BaseSchema


class RequestMetadataWithLinks(BaseSchema):

    links: RequestLinks
