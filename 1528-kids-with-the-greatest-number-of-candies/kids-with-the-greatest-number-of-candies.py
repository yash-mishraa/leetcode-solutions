class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        answer=[]
        for i in candies:
            answer.append(i+extraCandies>=maximum)
        return answer