import json
import os

def display_all(inventory):
    print("\nCurrent Inventory")
    print("-" * 48)

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("-" * 48)


def add_product(inventory):
    print("\nAdd New Product")

    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    product = {
        "id": product_id,
        "name": product_name,
        "price": price,
        "stock": stock
    }

    inventory.append(product)

    print("Product added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found:")
            print("Name:", product["name"])
            print("Current Stock:", product["stock"])

            new_stock = int(input("New Stock Quantity: "))

            product["stock"] = new_stock

            print("Stock updated successfully!")
            return

    print("Product not found.")


def search_product(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found")
            print("-" * 48)
            print("ID:", product["id"])
            print("Name:", product["name"])
            print(f"Price: ${product['price']:.2f}")
            print("Stock:", product["stock"])
            print("-" * 48)
            return

    print("Product not found.")