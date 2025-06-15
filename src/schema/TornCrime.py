import typing

from TornCrimeId import TornCrimeId

from ..base_schema import BaseSchema


class TornCrime(BaseSchema):

    unique_outcomes_ids: typing.List[int]
    unique_outcomes_count: int
    notes: typing.List[str]
    name: str
    id: TornCrimeId
    enhancer_name: str
    enhancer_id: int
    category_name: str
    category_id: int
