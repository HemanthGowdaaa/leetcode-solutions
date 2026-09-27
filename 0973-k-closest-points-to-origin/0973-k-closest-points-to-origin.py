class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        #select each element
        #calculate formula 
        #map the value and answer
        #create a heap
        #pop k elements
        heap = []
        for x,y in points:
            dist = (x**2)+(y**2)
            heap.append([dist,x,y])

        heapq.heapify(heap)
        # print(heap)
        res = []
        while k>0:
            dist,x,y = heapq.heappop(heap)
            res.append([x,y])
            k-=1
        return res