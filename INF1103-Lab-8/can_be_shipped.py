from abc import ABC, abstractmethod

class CanBeShipped(ABC):
    """Interface for products that can be shipped."""

    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        """Calculate the shipping cost."""
        pass
