# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            # Add item
            item = input("Type the item to add: ").strip()
            if item == "":
                print("You didn't type anything. Try again.")
            else:
                shopping_list.append(item)
                print(f"'{item}' was added to your shopping list.")

        elif choice == '2':
            # Remove item (case-insensitive)
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.")
                continue

            item = input("Type the item to remove: ").strip()
            if item == "":
                print("You didn't type anything. Try again.")
                continue

            # find a matching item ignoring letter case
            found_index = None
            for i, existing in enumerate(shopping_list):
                if existing.lower() == item.lower():
                    found_index = i
                    break

            if found_index is not None:
                removed = shopping_list.pop(found_index)
                print(f"'{removed}' was removed from your shopping list.")
            else:
                print(f"'{item}' was not found in the shopping list.")

        elif choice == '3':
            # View list
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\nYour shopping list:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")

        elif choice == '4':
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please type 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
