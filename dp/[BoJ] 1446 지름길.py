N, D = map(int, input().split())
dist_info = [ i for i in range(D + 1) ]
start_end_dist = [ list(map(int, input().split())) for _ in range(N)]
start_end_dist.sort(key = lambda x : (x[0], x[1], x[2]))

for cur in range(D + 1):
    
    dist_info[cur] = min(dist_info[cur] , dist_info[cur-1]+1)

    for start, end, dist in start_end_dist:
        if start == cur and end <= D and dist_info[end] > dist_info[cur] + dist :
            dist_info[end] = dist_info[cur] + dist

print(dist_info[D])

