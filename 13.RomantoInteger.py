class Solution(object):
    def romanToInt(self, s):
        roman_nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        roman_combinations = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        
        total = 0
        i = 0 
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in roman_combinations:
                two_char = s[i:i+2]
                total += roman_combinations[two_char]
                i+=2
            else:
                one_char = s[i]
                total += roman_nums[one_char]
                i+=1
        return total