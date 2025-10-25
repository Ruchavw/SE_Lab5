"""Inventory System Module
This script manages inventory items — add_ing, removing, saving, and checking stock levels.
"""

import json
from datetime import datetime

# Global variable
stock_data = {}

def add_item(item="default", qty=0, logs=None):
    """Adds a new item to the stock with quantity validation."""
    global stock_data

    if logs is None:
        logs=[]
    if not item:
        return
    
    # Validate types
    if not isinstance(item, (str, int)):
        print("Error: Item name or ID must be a string or integer.")
        return

    try:
        qty = int(qty)
        if qty < 0:
            print("Error: Quantity cannot be negative.")
            return
    except ValueError:
        print("Error: Quantity must be a number.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{str(datetime.now())}: Added {qty} of {item}")

def remove_item(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except Exception as e:
        print(f"Error occurred while removing item: {e}")

def get_qty(item):
    return stock_data[item]

def load_data(file="inventory.json"):
    with open(file, "r", encoding="utf-8") as f:
        global stock_data
        stock_data = json.loads(f.read())
        f.close()

def save_data(file="inventory.json"):
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))
        f.close()

def print_data():
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def check_low_items(threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print("Eval removed — printed safely.")

main()
