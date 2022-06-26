# binary_search.py
# Author: Euan Watkins
# Version: 1.0

# This class implements a binary search algorithm. This can only
# be used on sorted arrays. It will find a mid point in the array
# and eliminate the half where the search item cannot be. It repeats
# this until the item is found or the array cannot be split further.
def binary_search(self, array, search_item):

    # If the array is empty, the item cannot be found in it.
    if len(array) == 0:
        return False

    # Defines the mi point of the array. Use // to avoid floats.
    mid_point = array[len(array)//2]

    # If the item is found at the mid point return true.
    if mid_point == search_item:
        return True

    # If the item is less than the middle recursively call this method
    # on the first half of the array.
    elif search_item < mid_point:
        half = len(array)//2
        # Split the array in half. Store the first half. 
        # The : denotes which half you want.
        sub_array = array[:half]
        return binary_search(self, sub_array, search_item)

    # If the item is greater than the middle recursively call this
    # method on the second half of the array.
    elif search_item > mid_point:
        # If the item is greater than the largest item in the array
        # return false as it is not in the array.
        if search_item > array[len(array)-1]:
            return False
        half = len(array)//2
        # Split the array in half. Store the second half.
        sub_array = array[half:]
        return binary_search(self, sub_array, search_item)

    return False