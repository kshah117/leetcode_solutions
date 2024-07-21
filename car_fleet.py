from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ds = []
        for i in range(len(position)):
            ds.append((position[i], speed[i]))

        ds.sort(reverse=True)
        stack = []
        for c in ds:
            time = (target - c[0]) / c[1]
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
