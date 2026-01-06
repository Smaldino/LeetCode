class Solution(object):
    def isPalindrome(self, x):
        original = x 
        original_string = str(original)
        inverted_string = original_string[::-1]

        if original_string == inverted_string:
            return True
        else:
            return False
        
solution = Solution()

print(solution.isPalindrome(121))