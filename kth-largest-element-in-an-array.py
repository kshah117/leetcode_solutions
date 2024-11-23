class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg = [-x for x in nums]
        heapq.heapify(neg)
        while k > 1:
            heapq.heappop(neg)
            k -= 1
        return -heapq.heappop(neg)