cards = [13,11,10,7,4,3,2,0]
query = 7
output = 3

test = {
    "input":{
        "cards":[13,11,10,7,4,3,2,0],
        "query":11
    },
    "output":1
}


# def locate_cards(cards,query):
#     position = 0
#     while position < len(cards):
#         if cards[position] == query:
#             return position
#         position+=1
#         if position == len(cards):
#             return -1

# def test_location(cards,query,mid):
#     mid_number = cards[mid]
#     if mid_number == query:
#         if mid-1 >= 0 and cards[mid-1] == query:
#             return 'left'
#         else:
#             return 'found'
#     elif mid_number < query:
#         return 'left'
#     else:
#         return 'right'
    
# def locate_card(cards,query):
#     lo,hi = 0, len(cards)-1

#     while lo<=hi:
#         mid = (lo+hi)//2

#         result = test_location(cards,query,mid)
#         if result == 'found':
#             return mid
#         elif result == 'left':
#             hi = mid-1
#         elif result == 'right':
#             lo = mid + 1

#     return -1

nums = [5,7,7,8,8,10]

def binary_search(lo,hi,condition):
    while lo <= hi:
        mid = (lo+hi)//2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid-1
        else:
            lo = mid+1
    return -1

# def locate_card(cards,query):
#     def condition(mid):
#         if cards[mid] == query:
#             if mid > 0 and cards[mid-1] == query:
#                 return 'left'
#             else:
#                 return 'found'
#         elif cards[mid] < query:
#             return 'left'
#         else:
#             return 'right'
    
#     return binary_search(0,len(cards)-1,condition)


# result = locate_card(**test["input"]) == test["output"]
# print(result)

def first_position(nums,target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0,len(nums)-1,condition)

def last_position(nums,target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0,len(nums)-1,condition)   

def first_and_last_position(nums,target):
    return first_position(nums,target), last_position(nums,target)

result = first_and_last_position(nums,8)
print(result)