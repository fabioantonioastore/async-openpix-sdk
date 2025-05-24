from decimal import Decimal


class Serializer:
    @classmethod
    def decimal_to_int(cls, decimal: Decimal) -> int:
        return int(decimal * (10**2))
