from typing import Dict, Any

from openpix.utils import (
    WebhookEvent,
    Frequency,
    ChargeType,
    PixKeyType,
    TaxType,
    ApplicationType,
)


class Validators:
    @classmethod
    async def comment_validator(cls, comment: str) -> str:
        if len(comment) <= 140:
            return comment
        raise "Comment must have less than 140 characters"

    @classmethod
    async def day_generate_charge_validator(cls, day_generate_charge: int) -> int:
        if 1 <= day_generate_charge <= 31:
            return day_generate_charge
        raise "dayGenerateCharge must be a value between 1 and 31"

    @classmethod
    async def expires_in_validator(cls, expires_in: int) -> int:
        fifteen_minutes_in_seconds = 15 * 60
        if expires_in >= fifteen_minutes_in_seconds:
            return expires_in
        raise "expiresIn must have at least 15 minutes in seconds"

    @classmethod
    async def customer_model_validator(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        for key in data.keys():
            match key:
                case "phone":
                    return data
                case "email":
                    return data
                case "taxID":
                    return data
        raise "Customer must have at least name and phone or email or taxID"

    @classmethod
    async def day_due_validator(cls, day_due: int) -> int:
        if day_due >= 3:
            return day_due
        raise "dayDue must be greater or equal to 3"

    @classmethod
    async def webhook_event_validator(cls, event: str) -> str:
        if event in WebhookEvent:
            return event
        raise f"Invalid webhook event {event!r}"

    @classmethod
    async def frequency_validator(cls, frequency: str) -> str:
        if frequency in Frequency:
            return frequency
        raise f"Invalid frequency {frequency!r}"

    @classmethod
    async def charge_type_validator(cls, charge_type: str) -> str:
        if charge_type in ChargeType:
            return charge_type
        raise f"Invalid chargeType {charge_type!r}"

    @classmethod
    async def pix_key_type_validator(cls, pix_key_type: str) -> str:
        if pix_key_type in PixKeyType:
            return pix_key_type
        raise f"Invalid PixKeyType {pix_key_type!r}"

    @classmethod
    async def tax_type_validator(cls, tax_type: str) -> str:
        if tax_type in TaxType:
            return tax_type
        raise f"Invalid taxType {tax_type!r}"

    @classmethod
    async def application_type_validator(cls, application_type: str) -> str:
        if application_type in ApplicationType:
            return application_type
        raise f"Invalid applicationType {application_type!r}"
