class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        B = []
        for i in A:
            i = i*i
            B.append(i)
        #B=sorted(B)
        return sorted(B)