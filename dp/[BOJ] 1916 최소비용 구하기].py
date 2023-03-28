#N = 노드수, M = 간선수
#a, b , cost = 출발, 도착, 비용
#start, end =
#입력
import heapq
import sys
input = sys.stdin.readline
INF = 987654321

N = int(input())
M = int(input())
input_bus_data = [ list(map(int,input().split())) for i in range(M) ]
start, end = map(int,input().split())

node_info = [ [] for i in range(N + 1) ]
dist_info = [ INF for i in range(N + 1) ]
for a, b, cost in input_bus_data:
    node_info[a].append((b, cost))

#q는 (weight, node)
def dijstra(s):
    q = []
    heapq.heappush(q, [0, s])
    dist_info[s] = 0

    while q:
        cur_dist, cur_node = heapq.heappop(q)
        if dist_info[cur_node] < cur_dist: continue
        for next_node, weight in node_info[cur_node]:
            next_dist = cur_dist + weight
            if next_dist < dist_info[next_node]:
                dist_info[next_node] = next_dist
                heapq.heappush(q, [next_dist, next_node])
        
dijstra(start)
print(dist_info[end])