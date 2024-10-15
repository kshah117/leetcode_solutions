class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def helper_left():
            l = 0
            r = len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m -1
                else:
                    l = m + 1
            return l
        
        def helper_right():
            l = 0
            r = len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m -1
                else:
                    l = m + 1
            return r

        
        start = helper_left()
        end = helper_right()

        if start <= end:
            return [start, end]
        else:
            return [-1, -1]