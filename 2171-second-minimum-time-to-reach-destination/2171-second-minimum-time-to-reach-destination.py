import heapq as hq

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        distances = dict()
        secondDistances = dict()
        pq = []
        hq.heappush(pq, (0, 1))

        while len(pq) > 0:
            currTime, node = hq.heappop(pq)
            if node in secondDistances:
                continue
            if node in distances:
                if currTime == distances[node]:
                    continue
                secondDistances[node] = currTime
            else:
                distances[node] = currTime
            if (currTime % (2 * change)) >= change:
                currTime += (change - currTime % change)
            for neighbor in graph[node]:
                hq.heappush(pq, (currTime + time, neighbor))

        return secondDistances[n]