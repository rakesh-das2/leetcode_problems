from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        breakpoint()
        if length == 0:
            return False
        if length == 1:
            if flowerbed[0] == 1 and n == 0:
                return True
            elif flowerbed[0] == 0 and n == 1 or n == 0:
                return True
            elif flowerbed[0] == 1 or flowerbed[0] == 1 and n > 1:
                return False

        index = 1
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n = n - 1

        while index < length-1 and n > 0:

            if flowerbed[index-1] == 0 and flowerbed[index] == 0 and flowerbed[index+1] == 0:
                flowerbed[index] = 1
                n -= 1
            index += 1

        if flowerbed[-1] == 0 and flowerbed[-2] == 0 and n != 0:
            flowerbed[-1] = 1
            n -= 1

        if n < 1:
            return True
        else:
            return False


s = Solution()
input = [0, 1, 0]
print(s.canPlaceFlowers(input, 0))


# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
input = [1, 0, 0, 0, 1]
print(s.canPlaceFlowers(input, 1))
