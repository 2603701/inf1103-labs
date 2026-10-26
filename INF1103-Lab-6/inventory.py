from product import Product


class Inventory:
    """Manage a collection of Product objects."""

    def __init__(self):
        # Start with an empty list. Each item added should be a Product object.
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
        """Return the matching Product object, or None if it is not found."""
        for product in self.__products:
            if product.get_product_id().lower() == product_id.lower():
                return product

        return None

    def display_all(self) -> None:
        """Display every product currently in the inventory."""
        if not self.__products:
            print("Inventory is empty.")
            return

        print("\n--- Inventory ---")
        for product in self.__products:
            product.display_information()

    def get_all_products(self) -> list:
        """Return a copy of the product list for saving to JSON."""
        return self.__products.copy()
