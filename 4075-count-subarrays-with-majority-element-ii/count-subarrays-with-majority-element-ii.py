from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        offset = n + 2
        bit = [0] * (2 * n + 5)

        ans = 0
        prefix = 0

        idx = offset
        while idx < len(bit):
            bit[idx] += 1
            idx += idx & -idx

        m = len(bit)

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
            while i < m:
                bit[i] += 1
                i += i & -i

        return ans