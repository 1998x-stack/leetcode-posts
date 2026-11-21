from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        heap = []
        for value, frequency in counts.items():
            heapq.heappush(heap, (frequency, value))
            if len(heap) > k:
                heapq.heappop(heap)
        return [value for frequency, value in heap]
