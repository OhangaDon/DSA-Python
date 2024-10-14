nums = [4,2,6,3,4,6,2,1]

def merge_sort(nums):

    if len(nums) <= 1:
        return nums
    
    mid = len(nums) //2 

    left = nums[:mid]
    right = nums[mid:]

    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    sorted_nums = merge(left_sorted,right_sorted)

    return sorted_nums

def merge(nums1, nums2):
    merged = []
    i,j = 0,0

    while i<len(nums1) and j<len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]
    return merged + nums1_tail + nums2_tail


print(merge_sort(nums))