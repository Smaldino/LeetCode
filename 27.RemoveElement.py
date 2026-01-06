class Solution(object):
    def removeElement(self, nums, val):
        
        old_nums = nums
        new_nums = []
        value_to_remove = val
        
        for num in old_nums:
            if num != value_to_remove:
                new_nums.append(num)
                
        k = len(new_nums)
        
        underscores = ["_"] * (len(old_nums) - k)
        
        nums[:] = new_nums + underscores
        
        return k

solution = Solution()

nums1 = [3,2,2,3] 
val1 = 3
nums2 = [0,1,2,2,3,0,4,2] 
val2 = 2

k = solution.removeElement(nums2,val2)

print(f"New array:{nums2}")
print(f"k:{k}")

