
items = []                                      # Empty list

while True:                                     # Repeat menu
    print("\n1.Add  2.Remove  3.View  4.Sort  5.Quit")
    choice = input("Enter choice: ")             # Get choice
    if choice == "1":
        item = input("Enter item: ")             # Get item
        if item.lower() in [x.lower() for x in items]:  # Check duplicate
            print("Item already exists!")
        else:
            items.append(item)                  # Add item
    elif choice == "2":
        item = input("Enter item: ")             # Get item
        for x in items:                          # Check list
            if x.lower() == item.lower():       # Ignore case
                items.remove(x)                 # Remove item
                break
        else:
            print("Item not found!")             # Not in list
    elif choice == "3":
        print(items)
    elif choice == "4":
        items.sort()                             # Sort list
        print("List sorted!")
    elif choice == "5":
        break                                    # Exit program
    else:
        print("Invalid choice!")                 # Wrong choice