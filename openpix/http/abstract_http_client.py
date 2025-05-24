from abc import ABC
from typing import Optional


class AbstractHTTPClient(ABC):
    def __init__(self, base_url: str = "", timeout: Optional[float] = 5) -> None:
        self.base_url = base_url
        if len(self.base_url) > 0 and self.base_url[-1] != "/":
            self.base_url += "/"
        self.timeout = timeout
