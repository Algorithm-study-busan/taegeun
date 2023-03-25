#1. 노드(V), 간선(E)
#2. 시작 노드(S)
#3. 간선정보 (u,v,w) u---w---v

import heapq
from sys import stdin
input = stdin.readline

#input
v, e = map(int,input().split())
s = int(input())
edge_info = [list(map(int,input().split())) for i in range(e)] 
node_info = [ [] for i in range(v+1)]
dist_info = [ 987654321 for _ in range(v+1)]

for a, b, w in edge_info:
    node_info[a].append((b,w))

#heap 0 --> dist, 1 --> node
def dijstra(s):
    q = []
    heapq.heappush(q, [0, s])
    dist_info[s] = 0
    
    while q:
        cur_dist, cur_node = heapq.heappop(q)
        
        for next_node, dist_weight in node_info[cur_node]:
            next_dist = cur_dist + dist_weight
            if dist_info[next_node] > next_dist:
                dist_info[next_node] = next_dist
                heapq.heappush(q, [next_dist, next_node])
                

def main():
    dijstra(s)
    for i in dist_info[1:]:
        if i==987654321:
            print("INF")
        else:
            print(i)

main()
