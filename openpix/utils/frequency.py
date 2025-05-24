from enum import Enum


class Frequency(str, Enum):
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    BIMONTHLY = "BIMONTHLY"
    TRIMONTHLY = "TRIMONTHLY"
    SEMIANNUALY = "SEMIANNUALY"
    ANNUALY = "ANNUALY"