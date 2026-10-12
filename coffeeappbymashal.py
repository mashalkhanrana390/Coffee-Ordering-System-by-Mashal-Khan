
class coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class order:
    def __init__(self):
        self.items = []

    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to order..")

    def total(self):
        return sum(item.price for item in self.items)

    def show_order(self):
        if not self.items:
            print("No items in order..")
            return

        print("\nYOUR ORDER..")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price}")

        print(f"Total: ${self.total()}\n")

    def cheakout(self):
        if not self.items:
            print("Your cart is empty")
            return

        self.show_order()
        confirm = input("Proceed to checkout? (yes/no): ").strip().lower()

        if confirm == "yes":
            print("Order confirmed! Thank you..")
            self.items.clear()
        else:
            print("Checkout cancelled..")


def main():
    menu = [
        coffee("black", 2.5),
        coffee("Latte", 3.5),
        coffee("cappuccino", 3.0),
        coffee("cold", 4.0)
    ]

    my_order = order()

    while True:
        print("\n--- Coffee Menu ---")

        for i, item in enumerate(menu, 1):
            print(f"{i}. {item.name} - ${item.price}")

        print("5. View order")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice in ["1", "2", "3", "4"]:
            my_order.add_item(menu[int(choice) - 1])

        elif choice == "5":
            my_order.show_order()

        elif choice == "6":
            my_order.cheakout()

        elif choice == "7":
            print("Thanks for visiting. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
