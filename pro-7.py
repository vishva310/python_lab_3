def insertion_sort(arr):
    # Traverse from the second element to the end of the array
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

# Given list of elements
elements = [1, 4, 2, 8, 23]

# Perform insertion sort
insertion_sort(elements)

# Print sorted list
print("Sorted elements:", elements)
