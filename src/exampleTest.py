from sequentialSearch import sequential_search
from binarySearch import binary_search

# Example array to be searched and the item to search for.
array = [2,3,1]
search_item = 2

# Sequential Search test - prints whether or not item is found.
print("\nSequential Search:")
if sequential_search(sequential_search, array, search_item):
    print("Item Found\n")
else:
    print("Item Not Found\n")

# Binary Search test - prints whether or not item is found.
print("\nBinary Search:")
if binary_search(binary_search, array, search_item):
    print("Item Found\n")
else:
    print("Item Not Found\n")
