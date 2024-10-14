nums = [4,2,6,3,4,6,2,1]

def insertion_sort(nums):
    nums = list(nums)
    print(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        print("Current: ",cur)
        print("The value of i: ",i," The value of j: ",j)

        while j >=0 and nums[j] > cur:
            j -= 1
        

        nums.insert(j+1,cur)
        print(nums)

    return nums

print(insertion_sort(nums))