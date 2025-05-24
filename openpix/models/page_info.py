from dataclasses import dataclass
from typing import List, Any, Dict

from openpix.models import BaseModel


@dataclass
class PageInfo(BaseModel):
    errors: List[Dict[str, Any]]
    skip: int
    limit: int
    totalCount: int
    hasPreviousPage: bool
    hasNextPage: bool
