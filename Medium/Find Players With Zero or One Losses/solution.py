from collections import defaultdict
from typing import List


class Solution:

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        breakpoint()
        winners = defaultdict(int)
        loosers = defaultdict(int)
        for winner, looser in matches:
            winners[winner] += 1
            loosers[looser] += 1
        breakpoint()
        win_player = [
            player for player in winners if player not in loosers.keys()]
        loose_player = [player for player,
                        loosers_count in loosers.items() if loosers_count == 1]
        win_player.sort()
        loose_player.sort()
        return [win_player, loose_player]


# Example usage:
s = Solution()
data = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7],
        [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
result = s.findWinners(data)
print(result)
