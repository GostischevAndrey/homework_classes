from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    @abstractmethod
    def new_product(self, *args: Any, **kwargs: Any) -> Any:
        pass
