store_inventory = 0
failed_entries = 0

while store_inventory < 500:
    stock_quantity = input("Enter a stock quantity: ")
    if stock_quantity == "quit":
        print("Total Units Processed:", store_inventory)
        print("Number of Failed/Rejected Entries:", failed_entries)
        break
    elif not stock_quantity.isdigit() or int(stock_quantity) < 0:
        print("Invalid entry. Please enter a positive integer.")
        failed_entries += 1
        continue
    elif int(stock_quantity) > 500:
        print("Inventory limit exceeded")
    store_inventory += int(stock_quantity)
