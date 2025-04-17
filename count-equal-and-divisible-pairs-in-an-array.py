class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        N = len(nums)
        pairs = 0
        for i in range(N):
            for j in range(i + 1, N):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    pairs += 1
        return pairs


"""
More Optimized code 

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        def calculate_divisible_pairs(l):
            NL = len(l)
            pos_pairs = 0
            for i in range(NL):
                for j in range(i + 1, NL):
                    if (l[i] * l[j]) % k == 0:
                        pos_pairs += 1
            return pos_pairs

        N = len(nums)
        pairs = 0
        freq = {}

        for i in range(N):
            if freq.get(nums[i]):
                freq[nums[i]][0] += 1
                freq[nums[i]][1].append(i)
            else:
                freq[nums[i]] = [1, [i]]

        for val in freq.values():
            pos = val[1]
            pairs += calculate_divisible_pairs(pos)
        return pairs
"""