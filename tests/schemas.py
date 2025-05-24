from asyncio import run

from openpix.schemas import DiscountSettings, DiscountFixedDate


discount_settings = DiscountSettings(
    modality="test", discountFixedDate=[DiscountFixedDate(daysActive=1, value=12.45)]
)


async def main() -> None:
    print(await discount_settings.to_dict())
    print(discount_settings.discountFixedDate[0])
    print(discount_settings.discountFixedDate[0].value)
    print(await discount_settings.to_json())


run(main())
