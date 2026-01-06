class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        n = len(words)
        if not words:
            return -1
        else:
            return len(words[n-1])


solution = Solution()

s = "Hello World"
s = "luffy is still joyboy"
s = "   fly me   to   the moon  "

output = solution.lengthOfLastWord(s)
print(output)
