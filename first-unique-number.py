class FirstUnique:

    def __init__(self, nums: List[int]):
        self.map = Counter(nums)
        self.unique = -1
        for i in nums:
            if self.map[i] == 1:
                self.unique = i
                break

    def showFirstUnique(self) -> int:
        if self.unique == -1 or self.map[self.unique] > 1:
            for k, v in self.map.items():
                if v == 1:
                    self.unique = k
                    break
        if self.map[self.unique] > 1:
            self.unique = -1

        return self.unique

    def add(self, value: int) -> None:
        self.map[value] = self.map.get(value, 0) + 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
