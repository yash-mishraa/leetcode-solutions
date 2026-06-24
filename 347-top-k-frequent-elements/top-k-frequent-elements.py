from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_items=sorted(count.items(),key=lambda x:x[1], reverse = True)
        top_k = sorted_items[:k]
        result=[]
        return [num for num, freq in top_k]
