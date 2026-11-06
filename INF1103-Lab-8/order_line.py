from product import Product


class OrderLine:
    """Represent a product and its quantity in an order."""

    def __init__(self, product: Product, quantity: int):
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        """Calculate the subtotal for this order line."""
        return self.product.get_price() * self.quantity