class Solution(object):
    def plusOne(self, digits):
        
        string = ""
        result = []
        
        for digit in digits:
            string += str(digit)
        
        number = int(string) + 1
        
        for num in str(number):
            result.append(int(num))
        
        return result


solution = Solution()

digits = [9]
solution.plusOne(digits)