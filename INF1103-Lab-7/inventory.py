from product import Product

class Inventory:
    """Manage a collection of Product objects."""

    def __init__(self):
        self.__products = []

    def add_product(self, product: Product) -> bool:
        """Add a product unless its ID already exists."""
        if not isinstance(product, Product):
            return False

        if self.search_product(product.get_product_id()) is not None:
            return False

        self.__products.append(product)
        return True

    def search_product(self, product_id: str):
        """Search for a product using its ID."""
        for product in self.__products:
            if product.get_product_id().lower() == product_id.lower():
                return product

        return None

    def display_all(self) -> None:
        """Display all products."""
        if not self.__products:
            print("Inventory is empty.")
            return

        print("\n--- Inventory ---")

        for product in self.__products:
            product.display_information()
            print(f"Fulfilment: {product.get_fulfilment_info()}")

            if hasattr(product, "calculate_shipping_cost"):
                print(
                    f"Shipping Cost: "
                    f"${product.calculate_shipping_cost():.2f}"
                )

            print("-------------------------")

    def get_all_products(self) -> list:
        """Return a copy of the product list."""
        return self.__products.copy()
