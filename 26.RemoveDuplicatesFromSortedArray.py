
class Solution(object):
    def removeDuplicates(self, nums):
        
        unique_elements = []
        
        for num in nums:
            if num not in unique_elements:
                unique_elements.append(num)

        k = len(unique_elements)
        
        underscores = ["_"] * (len(nums) - k)
        nums[:] = unique_elements + underscores
        
        return k

solution = Solution()

nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]

k = solution.removeDuplicates(nums2)
print(f"Unique elements are {nums2}")
print(f"Number of unique elements is {k}")
