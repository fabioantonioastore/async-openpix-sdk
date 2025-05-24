from decimal import Decimal


class Serializer:
    @classmethod
    async def decimal_to_int(cls, decimal: Decimal) -> int:
        return int(decimal * (10**2))
