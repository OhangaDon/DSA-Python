nums = [22,11,88,44,66,55,77,33,44]

def quicksort(sequence):
    length = len(sequence)

    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    
    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)
    

    
print(quicksort(nums))

   