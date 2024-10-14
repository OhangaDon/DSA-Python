nums = [4,2,6,3,4,6,2,1]

def bubble_sort(nums):
    nums = list(nums)
    
    for _ in range(len(nums)-1):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
            print('inner loop:',nums)
        print('Outer loop:',nums)
    return nums

print(bubble_sort(nums))   