class Solution:

    def find_substring(s):
        start = result = 0
        index = {}
        for i, letter in enumerate(s):

            if index.get(letter, -1) >= start:
                start = index[letter]+1
            result = max(result, i-start+1)  # 0, 1, 3
            index[letter] = i

        return result


s1 = "abcabcdbb"
print(Solution.find_substring(s1))
