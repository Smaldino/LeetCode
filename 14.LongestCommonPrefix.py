class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for s in strs[1:]:
            while not s.startswith(prefix):
                print(prefix)
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                
        return prefix

solution = Solution()

strs = ["flower","flow","flight"]
print(f"The common prefix is -{solution.longestCommonPrefix(strs)}-")




