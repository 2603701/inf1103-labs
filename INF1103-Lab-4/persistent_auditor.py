def get_valid_input():
    while True:
        stock_quantity = input("Enter a stock quantity: ")
        if stock_quantity.lower() == "quit":
            return "quit"
        if not stock_quantity.isdigit() or int(stock_quantity) < 0:
            print("Invalid entry. Please enter a positive integer.")
            return None
        if int(stock_quantity) > 500:
            print("Inventory limit exceeded.")
            return None
        return int(stock_quantity)

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_units, deliveries_processed, failed_attempts): 
    print("Total Units Processed:", total_units) 
    print("Total Deliveries Processed:", deliveries_processed) 
    print("Number of Failed/Rejected Entries:", failed_attempts)
    
def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
            total_units = int(lines[0].split(":")[1].strip())
            transaction_history = []
            for line in lines[1:]:
                if line.strip():
                    transaction = int(line.split(":")[1].strip())
                    transaction_history.append(transaction)
            return total_units, transaction_history
    except FileNotFoundError:
        return 0, []
    
def save_inventory(total_units, transaction_history):
    with open("inventory.txt", "w") as file:
        file.write("Total Units: " + str(total_units) + "\n")
        for transaction in transaction_history:
            file.write("Transaction History: " + str(transaction) + "\n")

store_inventory, transaction_history = load_inventory()
failed_entries = 0
deliveries_processed = 0

while True:
    stock_quantity = get_valid_input()

    if stock_quantity == "quit":
        save_inventory(store_inventory, transaction_history)
        generate_report(store_inventory, deliveries_processed, failed_entries)
        break

    if stock_quantity is None:
        failed_entries += 1
        continue

    store_inventory = process_delivery(store_inventory, stock_quantity)

    if store_inventory > 500:
        print("Inventory limit exceeded.")
        break

    transaction_history.append(stock_quantity)
    tax = calculate_tax(stock_quantity)
    print("Tax for this delivery:", tax)
    deliveries_processed += 1
