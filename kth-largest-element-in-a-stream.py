class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums.copy()
        self.nums.sort()
        self.nums = self.nums[-k:]
        print(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            self.nums.append(val)
        else:
            if val > self.nums[0]:
                self.nums[0] = val
        self.nums.sort()
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)