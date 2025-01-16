class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        freq = {}
        N1, N2 = len(nums1), len(nums2)
        ret = 0
        for n1 in nums1:
            freq[n1] = freq.get(n1, 0) + N2
        
        for n2 in nums2:
            freq[n2] = freq.get(n2, 0) + N1

        for i in freq:
            if freq[i] % 2 == 1:
                ret ^= i

        return ret 
        