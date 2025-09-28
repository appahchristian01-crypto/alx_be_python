# shopping_list_manager.py

def display_menu():
    print("\n===== Shopping List Manager =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty list

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add item
            item = input("Enter the item to add: ").strip()
            if item:  # only add if not empty
                shopping_list.append(item)
                print(f"✅ '{item}' has been added to your shopping list.")
            else:
                print("⚠️ Item name cannot be empty.")

        elif choice == '2':
            # Remove item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"🗑️ '{item}' has been removed from your shopping list.")
            else:
                print(f"❌ '{item}' was not found in the list.")

        elif choice == '3':
            # View list
            if shopping_list:
                print("\n🛒 Your Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("\n📭 Your shopping list is currently empty.")

        elif choice == '4':
            # Exit
            print("👋 Goodbye!")
            break

        else:
            # Handle invalid choice
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

