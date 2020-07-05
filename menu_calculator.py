#!/usr/bin/env python3

MENU = {"1": ("Chicken strips", "3.50"),
        "2": ("French fries", "2.50"),
        "3": ("Hamburger", "4.00"),
        "4": ("Hotdog", "3.50"),
        "5": ("Large drink", "1.75"),
        "6": ("Medium drink", "1.50"),
        "7": ("Milk shake", "2.25"),
        "8": ("Salad", "3.75"),
        "9": ("Small drink", "1.25")
        }


def show_menu():
    """Display the menu for the user"""
    for k, v in MENU.items():
        print(f"{k}. {v[0]}: ${v[1]}")
    print()


def take_order():
    """Prompt user for customer's order"""
    print("Enter the number for each item you'd like to add to your order.")
    print("Don't include any spaces.")
    order = input()
    return order


def clean_order(order):
    """Remove any spaces or letters from input"""
    # Initialize empty string
    cleaned_order = ''

    # Concatenate just the numbers to the string
    for item in order:
        if item.isnumeric():
            cleaned_order += item

    return cleaned_order


def make_order_dict(order):
    """Build a dictionary to hold how many of each item was ordered"""
    order_dict = {}
    for item in order:
        order_dict[item] = order_dict.get(item, 0) + 1

    return order_dict


def find_item_cost(item):
    """Find item in dictionary, retrieve it's price, and convert to a float"""
    price = float(MENU[item][1])
    return price


def find_total_cost(order):
    """Find the order's total cost"""
    cost = 0

    for item in order:
        cost = cost + find_item_cost(item)
    return cost


def show_order_dict(order_dict, cost):
    """Format and display the customer's order"""
    print("Item".ljust(15) + "#".ljust(5) + "Order: ")

    for item, count in order_dict.items():
        print(MENU[item][0].ljust(14), count, ''.ljust(2), "$" + MENU[item][1])


def print_total(cost):
    """Format and print order's total cost"""
    cost = str(cost)
    if cost[-2:] == ".5":
        cost = cost + "0"
    print("-"*26)
    print("Total".ljust(20) + f"${cost}")


def verify_order():
    """Make sure order is correct"""
    correct = 'n'
    while correct != "y":
        print("\nIs this order correct? (y or n)")
        correct = input()
        if correct == "n":
            main()
        else:
            break


def main():
    # Initialize flag variable
    another_order = 'y'

    # Main program loop to be repeated as long as user wants
    while another_order == 'y':
        show_menu()

        # Have user input order and remove any invalid characters
        order = take_order()
        order = clean_order(order)

        # Convert the order to a dictionary for easier display and find cost
        order_dict = make_order_dict(order)
        cost = find_total_cost(order)

        # Display formatted order with total cost and verify
        show_order_dict(order_dict, cost)
        print_total(cost)
        verify_order()

        # Check if user wants to place another order
        another_order = input("Would you like to order again? (y or n)")


if __name__ == "__main__":
    main()
