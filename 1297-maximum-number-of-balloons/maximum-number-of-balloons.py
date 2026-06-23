from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text : str) -> int:
        Count = Counter(text)
        return min(
            Count['b'],
            Count['a'],
            Count['l']//2,
            Count['o']//2,
            Count['n']
        )