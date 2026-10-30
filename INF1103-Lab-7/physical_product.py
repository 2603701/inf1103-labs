from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    """Represent a physical product that requires shipping."""

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        weight: float
    ):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        """Display common information and product weight."""
        super().display_information()
        print(f"Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        """Calculate shipping cost based on weight."""
        return self.__weight * 2.50

    def to_dictionary(self) -> dict:
        data = super().to_dictionary()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data
