import typing

from BazaarSpecialized import BazaarSpecialized

from ..base_schema import BaseSchema


class BazaarResponseSpecialized(BaseSchema):

    bazaar: BazaarSpecialized
