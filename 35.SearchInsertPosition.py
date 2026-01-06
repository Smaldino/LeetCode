class Solution(object):
    def searchInsert(self, nums, target):
        
        n = len(nums)
        
        for i in range(n):
            if target == nums[i]:
                return i
            elif target < nums[i]:
                return i
        return n

solution = Solution()

# nums = [1,3,5,6] 
# target = 5

nums = [1,3,5,6]
target = 2

# nums = [1,3,5,6]
# target = 7

output = solution.searchInsert(nums, target)
print(output)
