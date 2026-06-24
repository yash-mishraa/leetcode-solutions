from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        evens=[]
        for x in nums :
            if x%2==0:
                evens.append(x)
        count=Counter(evens)
        if not evens:
            return -1
        sorted_items = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        return sorted_items[0][0]
