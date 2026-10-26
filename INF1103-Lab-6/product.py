class Product:
    """Represent one product in the inventory."""

    def __init__(self, product_id: str, name: str, price: float, stock: int):
        # Double underscores indicate attributes intended for internal use.
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    # Getter methods let other parts of the program read private attributes.
    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def update_stock(self, quantity: int) -> bool:
        """Set the stock to a new non-negative quantity. Return success/failure."""
        if not isinstance(quantity, int) or quantity < 0:
            return False

        self.__stock = quantity
        return True

    def display_information(self) -> None:
        """Print this product's information."""
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )

    def to_dictionary(self) -> dict:
        """Convert this object into a dictionary for JSON saving."""
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }
