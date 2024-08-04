def sequential_search(elements, target):
    for i in range(len(elements)):
        if elements[i] == target:
            return i 
    return -1 
elements = [1, 3, 5, 8, 10, 23, 35]
target = 10
result = sequential_search(elements, target)
if result != -1:
    print(f"Target value {target} found at index {result}.")
else:
    print(f"Target value {target} not found in the list.")
