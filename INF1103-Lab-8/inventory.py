from product import Product


class Inventory:
    """Manage a collection of Product objects."""

    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product) -> bool:
        """Add a product unless its ID already exists."""
        if not isinstance(product, Product):
            return False

        if self.find_product(product.get_product_id()) is not None:
            return False

        self.products.append(product)
        return True

    def remove_product(self, product_id: str) -> bool:
        """Remove a product using its ID."""
        product = self.find_product(product_id)

        if product is None:
            return False

        self.products.remove(product)
        return True

    def find_product(self, product_id: str) -> Product | None:
        """Find a product using its ID."""
        for product in self.products:
            if product.get_product_id().lower() == product_id.lower():
                return product

        return None

    def search_product(self, product_id: str) -> Product | None:
        """Search for a product (backwards-compatible method)."""
        return self.find_product(product_id)

    def display_all_products(self) -> None:
        """Display all products using polymorphism."""
        if not self.products:
            print("Inventory is empty.")
            return

        print("\n--- Inventory ---")

        for product in self.products:
            product.display_information()
            print(f"Fulfilment: {product.get_fulfilment_info()}")
            print("-------------------------")

    def display_all(self) -> None:
        """Display all products."""
        self.display_all_products()

    def get_all_products(self) -> list[Product]:
        """Return a copy of the product list."""
        return self.products.copy()