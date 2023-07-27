class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        elemn = 0
        while x > elemn:
            elemn = elemn * 10 + x % 10
            x = x // 10
        flag = (x == elemn or x == elemn // 10)
        return flag


s = Solution()
print(s.isPalindrome(x=121))
