class HitCounter:

    def __init__(self):
        self.hit_map = OrderedDict()

    def hit(self, timestamp: int) -> None:
        if timestamp in self.hit_map:
            self.hit_map[timestamp] += 1
        else:
            self.hit_map[timestamp] = 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for i in range(max(0, timestamp - 300) + 1, timestamp + 1):
            total += self.hit_map.get(i, 0)
        return total


        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)