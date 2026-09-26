import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        #heap 
        #max heap 
        # top two select 
        # pop two element 
        # insert new element if 
        heap = []
        for num in stones:
            heapq.heappush(heap,-num)
        print(heap)
        while len(heap)>1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x == y:
                continue
            if x !=y :
                heapq.heappush(heap,y-x)
        return -heap[0] if heap else 0

        