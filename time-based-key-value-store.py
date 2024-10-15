class TimeMap:

    def __init__(self):
        self.ts = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.ts.get(key):
            self.ts[key].append((value, timestamp))
        else:
            self.ts[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        ts_list = self.ts.get(key)

        if not ts_list or ts_list[0][1] > timestamp:
            return ""

        l = 0
        r = len(ts_list) - 1
        temp_ts = l

        while l <= r:
            if ts_list[l][1] > timestamp:
                break

            temp_ts = l

            m = (l + r) // 2

            if ts_list[m][1] == timestamp:
                return ts_list[m][0]
            elif ts_list[m][1] < timestamp:
                l = m + 1
            else:
                r = m - 1

        return ts_list[temp_ts][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
