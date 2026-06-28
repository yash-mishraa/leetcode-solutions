class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            seen=set()
            for j in range(n):
                num=matrix[i][j]

                if num < 1 or num > n :
                    return False
                
                if num in seen :
                    return False

                seen.add(num)

        for i in range(n):
            seen=set()
            for j in range(n):
                num=matrix[j][i]

                if num < 1 or num > n :
                    return False
                
                if num in seen :
                    return False

                seen.add(num)

        return True