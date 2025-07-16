import typing

from .torn_hof_basic import TornHofBasic
from .torn_hof_with_offenses import TornHofWithOffenses

TornHof = TornHofWithOffenses | TornHofBasic
