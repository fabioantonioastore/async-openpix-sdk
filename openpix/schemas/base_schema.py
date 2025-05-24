from typing import Dict, Any

from pydantic import BaseModel


class BaseSchema(BaseModel):
    async def to_dict(self) -> Dict[str, Any]:
        return self.model_dump()

    async def to_json(self) -> str:
        return self.model_dump_json()
