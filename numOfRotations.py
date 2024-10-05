test = {
    'input': {
        'nums':[19,25,29,3,5,6,7,9,11,14]
        },
        'output': 3
}

# def count_rotations(nums):
#     position = 1

#     while position < len(nums):
#         if position > 0 and nums[position] < nums[position-1]:
#             return position
#         position+=1

#     return 0

def count_rotations_binary(nums):
    lo = 0
    hi = len(nums) - 1
    
    while lo <= hi:
        mid = (hi + lo) // 2
        mid_number = nums[mid]

        # Check if mid is the rotation point
        if mid > 0 and mid_number < nums[mid - 1]:
            return mid
        
        # If mid_number >= nums[lo], search in the right half
        elif mid_number < nums[hi]:
            
            hi = mid - 1
        
        # Otherwise, search in the left half
        else:
            lo = mid + 1
    return 0  # If no rotation is


nums = test['input']['nums']
output = test['output']
result = count_rotations_binary(nums)
print(result)