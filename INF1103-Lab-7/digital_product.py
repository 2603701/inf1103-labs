from product import Product

class DigitalProduct(Product):
    """Represent a digital product delivered electronically."""

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        download_size: float
    ):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        """Display common information and download size."""
        super().display_information()
        print(f"Download Size: {self.__download_size:.2f} MB")

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."

    def to_dictionary(self) -> dict:
        data = super().to_dictionary()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data
