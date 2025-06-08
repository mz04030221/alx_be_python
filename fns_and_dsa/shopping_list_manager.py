def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            shopping_list.append(input("Enter the item to add: "))
            pass
        elif choice == '2':
            del shopping_list[int(input("Choose an item to remove: ")) - 1]
            pass
        elif choice == '3':
            for i in shopping_list:
                print(f"{i + 1} {shopping_list[i]}")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
