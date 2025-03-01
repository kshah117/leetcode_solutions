class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        
        cur_range = 0
        farthest = 0
        jumps = 0

        for i in range(N - 1):
            farthest = max(farthest, nums[i] + i)

            if i == cur_range:
                jumps += 1
                cur_range = farthest
            
            if cur_range >= N - 1:
                return jumps
        return jumps

