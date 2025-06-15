import typing

from CompanyId import CompanyId

from ..base_schema import BaseSchema


class ReportHistoryCompany(BaseSchema):

    name: str
    left: None | str
    joined: str
    id: CompanyId
