from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order


def show_product_details(product: Product) -> None:
    """Demonstrate Liskov Substitution Principle."""
    product.display_information()
    print(product.get_fulfilment_info())


def test_lab8():

    # 1. Association: Supplier and Product
    print("\n===== ASSOCIATION =====")

    supplier = Supplier(
        "S001",
        "Tech Supplier",
        "tech@example.com"
    )

    physical = PhysicalProduct(
        "P001",
        "Keyboard",
        50.00,
        20,
        0.8,
        supplier
    )

    digital = DigitalProduct(
        "D001",
        "Antivirus Software",
        30.00,
        50,
        100.0,
        supplier
    )

    physical.get_supplier().display_information()
    digital.get_supplier().display_information()

    assert physical.get_supplier() is supplier
    assert digital.get_supplier() is supplier

    print("Association test passed!")

    # 2. Aggregation: Inventory and Product
    print("\n===== AGGREGATION =====")

    inventory_a = Inventory()
    inventory_b = Inventory()

    assert inventory_a.add_product(physical)

    print("Product added to Inventory A.")

    assert inventory_a.remove_product("P001")

    print("Product removed from Inventory A.")

    # Product still exists after removal.
    physical.display_information()

    assert inventory_b.add_product(physical)

    print("Product transferred to Inventory B.")

    assert inventory_b.find_product("P001") is physical

    print("Aggregation test passed!")

    # 3. Composition: Order and OrderLine
    print("\n===== COMPOSITION =====")

    order1 = Order("ORD001")

    order1.add_order_line(physical, 2)
    order1.add_order_line(digital, 3)

    order1.display_order()

    # Add the same Product to another Order.
    order2 = Order("ORD002")

    order2.add_order_line(physical, 1)

    # Two different OrderLine objects.
    assert order1.order_lines[0] is not order2.order_lines[0]

    # Both OrderLines refer to the same Product.
    assert order1.order_lines[0].product is order2.order_lines[0].product

    print("Composition test passed!")

    # 4. LSP and Polymorphism
    print("\n===== LSP AND POLYMORPHISM =====")

    products: list[Product] = [
        physical,
        digital
    ]

    for product in products:
        show_product_details(product)
        print("-------------------------")

    print("LSP and Polymorphism tests passed!")

    print("\nAll Lab 8 tests completed successfully!")


if __name__ == "__main__":
    test_lab8()