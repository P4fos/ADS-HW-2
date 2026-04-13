import heapq

def top_k_frequent(nums, k):
    d = {}

    for x in nums:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    heap = []

    for key in d:
        heapq.heappush(heap, (d[key], key))

        if len(heap) > k:
            heapq.heappop(heap)

    ans = []

    while len(heap) > 0:
        ans.append(heapq.heappop(heap)[1])

    return ans