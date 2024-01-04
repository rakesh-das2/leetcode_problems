class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str2+str1 != str1+str2:
            return ""
        a = len(str1)
        b = len(str2)
        while b:
            a, b = b, a % b
        return str1[:a]


s = Solution()
# str1 = "ABCABC" and str2 = "ABC"
# Output "ABC"
print(s.gcdOfStrings("ABCABC", "ABC"))
# str1 = "ABAB" and str2 = "AB"
# Output "AB"
print(s.gcdOfStrings("ABAB", "AB"))
# str1 = "LEET" and str2 = "CODE"
# Output ""
print(s.gcdOfStrings("LEET", "CODE"))
# str1 = "ABCDEF" and str2 = "ABC"
# Output ""
print(s.gcdOfStrings("ABCDEF", "ABC"))
