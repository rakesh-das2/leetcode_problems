

def reverseVowels(s):
    data = list(s)
    start, end = 0, len(data)-1
    vowels = "aeiouAEIOU"
    breakpoint()
    while start <= end:
        while start < end and data[start] not in vowels:
            start += 1
        while start < end and data[end] not in vowels:
            end -= 1
        data[start], data[end] = data[end], data[start]
        start += 1
        end -= 1
    return "".join(data)


# Input: s = "leetcode"
# Output: "leotcede"

s = "leetcode"
print(reverseVowels(s))


# Input: s = "hello"
# Output: "holle"
s = "hello"
print(reverseVowels(s))
