class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums)
        
        def helper(s):
            if len(s) > N:
                return

            if len(s) == N and s not in nums:
                return s
            
            for i in ["0", "1"]:
                temp = s + i
                val = helper(temp)
                if val:
                    return val
            
        return helper("")