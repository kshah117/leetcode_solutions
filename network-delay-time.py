class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        dist = {}

        for u, v, w in times:
            graph[u].append((v, w))

        heap = []
        heappush(heap, (0, k))

        while heap:
            time, cur_node = heappop(heap)
            if cur_node in dist:
                continue

            dist[cur_node] = time
            neighbors = graph[cur_node]

            for neighbor, weight in neighbors:
                if neighbor not in dist:
                    heappush(heap, (time + weight, neighbor))

        return max(dist.values()) if len(dist) == n else -1
