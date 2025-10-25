"""Inventory System Module
This script manages inventory items —
    add_ing, removing, saving, and checking stock levels.
"""

import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add a new item or increase quantity in the stock.

    Args:
        item (str | int): The name or ID of the item.
        qty (int | str): Quantity to be added.
        logs (list, optional): List to store log entries.

    Notes:
        Performs type validation, prevents negative or invalid quantities,
        and appends a log entry for every addition.
    """
    global stock_data

    if logs is None:
        logs = []
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
    """Remove an item or decrease its quantity from stock.

    Args:
        item (str | int): The item to remove.
        qty (int): Quantity to remove.

    Handles missing items and logs an error if removal fails.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except Exception as e:
        print(f"Error occurred while removing item: {e}")


def get_qty(item):
    """Return the quantity of a specific item from stock.

    Args:
        item (str | int): The item name or ID.

    Returns:
        int: Quantity available for the item.
    """
    return stock_data[item]


def load_data(file="inventory.json"):
    """Load stock data from a JSON file.
    Args:
        file (str): Path to the inventory file.
    Notes:
        Opens the file with UTF-8 encoding for safety."""
    with open(file, "r", encoding="utf-8") as f:
        global stock_data
        stock_data = json.loads(f.read())
        f.close()


def save_data(file="inventory.json"):
    """Save current stock data to a JSON file.

    Args:
        file (str): Path to the inventory file.

    Notes:
        Writes JSON with UTF-8 encoding to ensure cross-platform compatibility.
    """
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))
        f.close()


def print_data():
    """Print all current items and their quantities."""
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])


def check_low_items(threshold=5):
    """Return a list of items with quantities below a threshold.

    Args:
        threshold (int): Minimum acceptable quantity.

    Returns:
        list[str]: Items with stock lower than the threshold.
    """
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """Main function to demonstrate the inventory system workflow."""
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
