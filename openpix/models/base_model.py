import json
from dataclasses import dataclass, asdict, astuple
from typing import Dict, Any, Tuple


@dataclass
class BaseModel:
    async def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    async def to_tuple(self) -> Tuple[Any, ...]:
        return astuple(self)

    async def to_json(self) -> str:
        return json.dumps(await self.to_dict())
