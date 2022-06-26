# sequential_search.py
# Author: Euan Watkins
# Version: 1.0

# This class implements a sequential search algorithm which goes
# through each array item one by one. It stops when the item is
# found or the end of the array is reached.
def sequential_search(self, array, search_item):
        for i in array:
            if i == search_item:
                # Return true if the item has been found.
                return True
        # Return false if the item was not found.
        return False