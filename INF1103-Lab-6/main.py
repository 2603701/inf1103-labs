import json
from pathlib import Path

from product import Product
from inventory import Inventory

# Store inventory.json in the same folder as this Python file.
DATA_FILE = Path(__file__).with_name("inventory.json")


def load_inventory() -> Inventory:
    """Load products from JSON and convert them into Product objects."""
    inventory = Inventory()

    if not DATA_FILE.exists():
        return inventory

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            saved_products = json.load(file)

        for item in saved_products:
            product = Product(
                item["product_id"],
                item["name"],
                float(item["price"]),
                int(item["stock"]),
            )
            inventory.add_product(product)

    except (json.JSONDecodeError, OSError, KeyError, TypeError, ValueError) as error:
        print(f"Could not load inventory file: {error}")

    return inventory


def save_inventory(inventory: Inventory) -> None:
    """Convert Product objects to dictionaries and save them as JSON."""
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
    """Ask for product details and add a new product."""
    product_id = input("Enter product ID: ").strip()
    name = input("Enter product name: ").strip()

    try:
        price = float(input("Enter product price: $"))
        stock = int(input("Enter stock quantity: "))
    except ValueError:
        print("Invalid input. Price must be a number and stock must be a whole number.")
        return

    if not product_id or not name:
        print("Product ID and name cannot be empty.")
        return

    if price < 0 or stock < 0:
        print("Price and stock cannot be negative.")
        return

    product = Product(product_id, name, price, stock)

    if inventory.add_product(product):
        print("Product added successfully.")
    else:
        print("A product with that ID already exists.")


def update_stock_menu(inventory: Inventory) -> None:
    """Find a product and update its stock quantity."""
    product_id = input("Enter the product ID: ").strip()
    product = inventory.search_product(product_id)

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
    """Search for a product and display it if found."""
    product_id = input("Enter the product ID to search: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
    else:
        print("Product found:")
        product.display_information()


def main() -> None:
    """Run the inventory menu."""
    inventory = load_inventory()
    print("Welcome to the Inventory Management System!")

    while True:
        print("\n===== Inventory Menu =====")
        print("1. Display all products")
        print("2. Add a product")
        print("3. Update stock")
        print("4. Search for a product")
        print("5. Save inventory")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product_menu(inventory)
        elif choice == "3":
            update_stock_menu(inventory)
        elif choice == "4":
            search_product_menu(inventory)
        elif choice == "5":
            save_inventory(inventory)
        elif choice == "6":
            # Save before exiting so recent changes are not lost.
            save_inventory(inventory)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
