from pydantic import field_validator

from openpix.schemas import BaseSchema
from openpix.utils import Validators


class Application(BaseSchema):
    name: str
    type: str

    @field_validator("type")
    async def application_type_validator(self, value: str) -> str:
        return await Validators.application_type_validator(value)


class ApplicationDelete(BaseSchema):
    clientId: str


class ApplicationCreate(BaseSchema):
    accountId: str
    application: Application