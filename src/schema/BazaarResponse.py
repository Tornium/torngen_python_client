import typing

from BazaarSpecialized import BazaarSpecialized
from BazaarWeekly import BazaarWeekly

from ..base_schema import BaseSchema


class BazaarResponse(BaseSchema):

    bazaar: BazaarSpecialized | BazaarWeekly
