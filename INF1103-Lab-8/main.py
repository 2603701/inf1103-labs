import json
from pathlib import Path

from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from supplier import Supplier
from order import Order
from can_be_shipped import CanBeShipped


DATA_FILE = Path(__file__).with_name("inventory.json")


def load_inventory() -> Inventory:
    """Load products from JSON and create the appropriate objects."""

    inventory = Inventory()

    if not DATA_FILE.exists():
        return inventory

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            saved_products = json.load(file)

        for item in saved_products:

            product_type = item["type"]

            # Load supplier information.
            # The default values support older Lab 7 JSON records.
            supplier_data = item.get("supplier", {})

            supplier = Supplier(
                supplier_data.get("supplier_id", "SUP-DEFAULT"),
                supplier_data.get("name", "Unknown Supplier"),
                supplier_data.get(
                    "contact_email",
                    "not-provided@example.com"
                )
            )

            if product_type == "physical":

                product = PhysicalProduct(
                    item["product_id"],
                    item["name"],
                    float(item["price"]),
                    int(item["stock"]),
                    float(item["weight"]),
                    supplier
                )

            elif product_type == "digital":

                product = DigitalProduct(
                    item["product_id"],
                    item["name"],
                    float(item["price"]),
                    int(item["stock"]),
                    float(item["download_size"]),
                    supplier
                )

            else:
                print(f"Unknown product type: {product_type}")
                continue

            if not inventory.add_product(product):
                print(f"Skipped duplicate product ID: {item['product_id']}")

    except (
        json.JSONDecodeError,
        OSError,
        KeyError,
        TypeError,
        ValueError
    ) as error:

        print(f"Could not load inventory file: {error}")

    return inventory


def save_inventory(inventory: Inventory) -> None:
    """Save all products into JSON."""

    products_to_save = [
        product.to_dictionary()
        for product in inventory.get_all_products()
    ]

    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(products_to_save, file, indent=4)

        print("Inventory saved successfully.")

    except OSError as error:
        print(f"Could not save inventory file: {error}")


def add_product_menu(inventory: Inventory) -> None:
    """Add either a physical or digital product."""

    print("\n--- Add Product ---")
    print("1. Physical Product")
    print("2. Digital Product")

    choice = input("Choose product type (1-2): ").strip()

    if choice not in ("1", "2"):
        print("Invalid product type.")
        return

    product_id = input("Enter product ID: ").strip()
    name = input("Enter product name: ").strip()

    if not product_id or not name:
        print("Product ID and name cannot be empty.")
        return

    if inventory.find_product(product_id) is not None:
        print("A product with that ID already exists.")
        return

    try:
        price = float(input("Enter product price: $"))
        stock = int(input("Enter stock quantity: "))

        if price < 0 or stock < 0:
            print("Price and stock cannot be negative.")
            return

        # Create Supplier independently.
        print("\n--- Supplier Information ---")

        supplier_id = input("Enter supplier ID: ").strip()
        supplier_name = input("Enter supplier name: ").strip()
        contact_email = input("Enter supplier email: ").strip()

        if not supplier_id or not supplier_name or not contact_email:
            print("Supplier information cannot be empty.")
            return

        supplier = Supplier(
            supplier_id,
            supplier_name,
            contact_email
        )

        # Create the appropriate product.
        if choice == "1":

            weight = float(input("Enter product weight (kg): "))

            if weight < 0:
                print("Weight cannot be negative.")
                return

            product = PhysicalProduct(
                product_id,
                name,
                price,
                stock,
                weight,
                supplier
            )

        else:

            download_size = float(
                input("Enter download size (MB): ")
            )

            if download_size < 0:
                print("Download size cannot be negative.")
                return

            product = DigitalProduct(
                product_id,
                name,
                price,
                stock,
                download_size,
                supplier
            )

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    if inventory.add_product(product):
        print("Product added successfully.")
    else:
        print("Unable to add product.")


def update_stock_menu(inventory: Inventory) -> None:
    """Update the stock quantity of a product."""

    product_id = input("Enter the product ID: ").strip()
    product = inventory.find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    try:
        new_stock = int(input("Enter the new stock quantity: "))

    except ValueError:
        print("Stock must be a whole number.")
        return

    if product.update_stock(new_stock):
        print("Stock updated successfully.")
    else:
        print("Stock cannot be negative.")


def search_product_menu(inventory: Inventory) -> None:
    """Search and display a product."""

    product_id = input("Enter the product ID to search: ").strip()
    product = inventory.find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("\nProduct found:")
    product.display_information()

    print(f"Fulfilment: {product.get_fulfilment_info()}")

    print("\nSupplier Information:")
    product.get_supplier().display_information()

    if isinstance(product, CanBeShipped):
        print(
            f"Shipping Cost: "
            f"${product.calculate_shipping_cost():.2f}"
        )


def create_order_menu(inventory: Inventory) -> None:
    """Create a customer order."""

    print("\n--- Create Customer Order ---")

    order_id = input("Enter order ID: ").strip()

    if not order_id:
        print("Order ID cannot be empty.")
        return

    order = Order(order_id)

    while True:

        product_id = input(
            "\nEnter product ID (or press Enter to finish): "
        ).strip()

        if not product_id:
            break

        product = inventory.find_product(product_id)

        if product is None:
            print("Product not found.")
            continue

        try:
            quantity = int(input("Enter quantity: "))

            order.add_order_line(product, quantity)

            print("Product added to order successfully.")

        except ValueError as error:
            print(f"Invalid quantity: {error}")

    order.display_order()


def main() -> None:
    """Run the Inventory Management System."""

    inventory = load_inventory()

    print("Welcome to the Inventory Management System!")

    while True:

        print("\n===== Inventory Menu =====")
        print("1. Display all products")
        print("2. Add a product")
        print("3. Update stock")
        print("4. Search for a product")
        print("5. Save inventory")
        print("6. Create customer order")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            inventory.display_all_products()

        elif choice == "2":
            add_product_menu(inventory)

        elif choice == "3":
            update_stock_menu(inventory)

        elif choice == "4":
            search_product_menu(inventory)

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            create_order_menu(inventory)

        elif choice == "7":
            save_inventory(inventory)
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()