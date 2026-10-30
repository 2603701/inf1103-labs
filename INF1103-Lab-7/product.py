from abc import ABC, abstractmethod

class Product(ABC):
    """Represent a general product in the inventory."""

    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def update_stock(self, quantity: int) -> bool:
        """Update stock to a non-negative quantity."""
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity < 0:
            return False

        self.__stock = quantity
        return True

    def display_information(self) -> None:
        """Display common product information."""
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Return how the product will be fulfilled."""
        pass

    def to_dictionary(self) -> dict:
        """Convert product information into a dictionary."""
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }
