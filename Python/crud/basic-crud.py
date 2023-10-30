# Define an empty list to store items
items = []

# Function to create (C) a new item
def create_item(item):
    items.append(item)
    print(f"Item '{item}' added successfully.")

# Function to read (R) all items
def read_items():
    if items:
        print("List of items:")
        for i, item in enumerate(items, start=1):
            print(f"{i}. {item}")
    else:
        print("No items in the list.")

# Function to update (U) an item
def update_item(index, new_item):
    if index >= 0 and index < len(items):
        items[index] = new_item
        print(f"Item updated at index {index}.")
    else:
        print("Invalid index. Item not updated.")

# Function to delete (D) an item
def delete_item(index):
    if index >= 0 and index < len(items):
        deleted_item = items.pop(index)
        print(f"Item '{deleted_item}' deleted.")
    else:
        print("Invalid index. Item not deleted.")

# Main program loop
while True:
    print("\nCRUD Menu:")
    print("1. Create item")
    print("2. Read items")
    print("3. Update item")
    print("4. Delete item")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        item = input("Enter the item to add: ")
        create_item(item)
    elif choice == '2':
        read_items()
    elif choice == '3':
        index = int(input("Enter the index of the item to update: "))
        new_item = input("Enter the new item: ")
        update_item(index - 1, new_item)
    elif choice == '4':
        index = int(input("Enter the index of the item to delete: "))
        delete_item(index - 1)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5).")

# End of the program
