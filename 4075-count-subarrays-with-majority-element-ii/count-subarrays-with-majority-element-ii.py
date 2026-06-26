from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        size = 2 * n + 5
        offset = n + 2
        bit = [0] * size

        prefix = 0
        ans = 0

        i = offset
        while i < size:
            bit[i] += 1
            i += i & -i

        for x in nums:
            prefix += 1 if x == target else -1
            idx = prefix + offset
            s = 0
            i = idx - 1
            while i:
                s += bit[i]
                i -= i & -i
            ans += s
            i = idx
            while i < size:
                bit[i] += 1
                i += i & -i

        return ans