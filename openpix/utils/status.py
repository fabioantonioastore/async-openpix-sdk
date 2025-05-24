from enum import Enum


class Status(str, Enum):
    IN_PROCESSING = "IN_PROCESSING"
    CONFIRMED = "CONFIRMED"
    REJECTED = "REJECTED"
