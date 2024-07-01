class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_map = {}
        for i, x in enumerate(ring):
            if ring_map.get(x):
                ring_map[x].append(i)
            else:
                ring_map[x] = [i]

        cache_map = {}

        def helper(curr_index, ring_pos):
            if curr_index == len(key):
                return 0

            if cache_map.get((ring_pos, curr_index)):
                return cache_map[(ring_pos, curr_index)]

            dist_arr = ring_map[key[curr_index]]

            res = float("inf")
            for ri in dist_arr:
                dist = min(abs(ring_pos - ri), len(ring) - abs(ring_pos - ri)) + 1
                res = min(res, dist + helper(curr_index + 1, ri))

            cache_map[(ring_pos, curr_index)] = res
            return res

        min_moves = helper(0, 0)
        return min_moves


sol = Solution()
print(sol.findRotateSteps(ring="godding", key="gd"))
