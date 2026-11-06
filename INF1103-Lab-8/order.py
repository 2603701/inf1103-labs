from product import Product
from order_line import OrderLine


class Order:
    """Represent a customer order."""

    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(
        self,
        product: Product,
        quantity: int
    ) -> None:
        """Create and add an OrderLine to the order."""

        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, index: int) -> bool:
        """Remove an order line using its index."""

        if index < 0 or index >= len(self.order_lines):
            return False

        self.order_lines.pop(index)
        return True

    def calculate_total(self) -> float:
        """Calculate the total value of the order."""

        total = 0.0

        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()

        return total

    def display_order(self) -> None:
        """Display all order lines and the total."""

        print(f"\n--- Order: {self.order_id} ---")

        if not self.order_lines:
            print("This order is empty.")
            return

        for index, order_line in enumerate(self.order_lines, start=1):
            print(
                f"{index}. {order_line.product.get_name()} | "
                f"Quantity: {order_line.quantity} | "
                f"Subtotal: ${order_line.calculate_subtotal():.2f}"
            )

        print("-------------------------")
        print(f"Order Total: ${self.calculate_total():.2f}")