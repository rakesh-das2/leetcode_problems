# Problem Statement
<img width="617" alt="image" src="https://github.com/CodeWithRakesh-stack/leetcode_problems/assets/43961504/bcc5cc61-fbc8-4d06-8f7b-4b76f11b9070">


# Approach With Hashtable
**Enumerate through the string:**
enumerate is a built-in Python function that returns both the index and value of each element in an iterable. In this case, it is used to iterate through each character of the input string.Store character as key and index as value in the dictionary:
As the loop iterates through the string, a dictionary (dict) is used to store the characters encountered so far as keys and their corresponding index as values.This is done to keep track of the last known index where each character appeared.

**Check max between earlier result and index-start+1:**
For each character in the string, the algorithm calculates the current length of the substring without repeating characters.
It compares this length with the maximum length seen so far result and updates result accordingly.

**If the dictionary contains the character as a key:**
If the character is already in the dictionary, it means it has been encountered before in the current substring.
The algorithm checks whether the stored index of the character in the dictionary (dict[letter]) is greater than or equal to the current starting position (start). 
This is to ensure that the repeated character is part of the current substring being considered.If the condition is true, it means the repeated character is within the current substring, so the starting position is updated to dict[letter] + 1. This effectively moves the starting position to the next index after the last occurrence of the repeated character.





class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = result = 0
        index = {}
        start_index = 0
        for i, letter in enumerate(s):
            if index.get(letter, -1) >= start:
                start = index[letter]+1
                    
            result = max(result, i-start+1)
            index[letter] = i
        return result
