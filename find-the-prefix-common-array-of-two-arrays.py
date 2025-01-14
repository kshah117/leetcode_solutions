class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        prefix = [0] * len(A)
        if A[0] == B[0]:
            prefix[0] = 1
        for i in range(1, len(A)):
            prefix[i] += prefix[i - 1]
            if A[i] == B[i]:
                prefix[i] += 1
                continue
            if B[i] in A[:i]:
                prefix[i] += 1
            if A[i] in B[:i]:
                prefix[i] += 1

        return prefix