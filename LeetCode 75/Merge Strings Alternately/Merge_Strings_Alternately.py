class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        count = 0
        new_word = ""
        while count < min(len(word1), len(word2)):
            new_word = new_word+word1[count]+word2[count]
            count += 1

        return new_word + word1[count:]+word2[count:]


s = Solution()
print(s.mergeAlternately("abc", "pqr"))
# Output: "apbqcr"

# Input: word1 = "ab", word2 = "ab"
print(s.mergeAlternately("ab", "ab"))
# Output: "apbqrs"
