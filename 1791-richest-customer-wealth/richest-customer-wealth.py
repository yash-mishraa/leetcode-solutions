class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxw=0
        for i in accounts:
            wealth=sum(i)

            if wealth>maxw:
                maxw=wealth
        return maxw