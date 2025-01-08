# Written by Craig'n'Dave
# Binary search using an array/list
def binary_search(items, item_to_find):
    found = False
    first = 0
    last = len(items) - 1
    # Repeat until the item is found or no items are left to check
    while first <= last and not found:
        # Calculate the mid point using integer division
        midpoint = (first + last) // 2
        # Item found
        if items[midpoint] == item_to_find:
            found = True
        else:
            # Recalculate the mid point
            if items[midpoint] < item_to_find:
                first = midpoint + 1
            else:
                last = midpoint - 1
    if found:
        print("Item found at position", midpoint)
    else:
        print("Item not found")


items = ["Alabama", "California", "Delaware", "Florida", "Georgia"]
item_to_find = input("Enter the state to find: ")
binary_search(items, item_to_find)
