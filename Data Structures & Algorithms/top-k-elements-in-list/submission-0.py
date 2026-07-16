import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict()
        heap = []
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
    
        for key, value in freq.items():
            tup = (value, key)
            if len(heap) < k:
                heapq.heappush(heap, tup)
            else:
                heapq.heappushpop(heap, tup)
        
        return [heap[i][1] for i in range(k)]