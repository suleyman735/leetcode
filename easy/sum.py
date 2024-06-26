

def sumTwo(nums, target):
    to_keep_index_and_values = {}  
    for i, num in enumerate(nums):
        complement = target - num
        if complement in to_keep_index_and_values:
            return [to_keep_index_and_values[complement], i]
        to_keep_index_and_values[num] = i
    return []
                 
print(sumTwo([2, 7, 11, 15], 9))  # Output: [0, 1]
print(sumTwo([3, 2, 4], 6))       # Output: [1, 2]
print(sumTwo([3, 3], 6))  