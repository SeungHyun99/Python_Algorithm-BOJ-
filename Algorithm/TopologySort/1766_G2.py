# 1766 / 문제집[G3]
    # https://www.acmicpc.net/problem/1766

    # 각 노드간의 순서가 있고, 같은 위치(InDegree==0)끼리는 숫자가 더 낮은 노드가 먼저 나가기
        # └> 위상정렬의 답이 1개
    # heapq를 이용한 위상정렬

import heapq
import sys
input = sys.stdin.readline

    # input
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
in_degree = [0]*(n+1)
in_degree[0] = -1
for _ in range(m):
    a,b = map(int,input().split())
    in_degree[b] += 1
    graph[a].append(b)

    # initialization
queue = []
for i in range(1,n+1):
    if in_degree[i] == 0:
        heapq.heappush(queue,i)
answer = []

    # Topology Sort
while queue:
    cur = heapq.heappop(queue)
    answer.append(cur)

    for j in graph[cur]:    # 현재 노드 뒷노드들의 in_degree -1
        in_degree[j] -= 1
        if in_degree[j] == 0:   # indegree == 0이면 heapq에 추가
            heapq.heappush(queue,j) # in_degree==0의 의미: 앞에 있어야하는 노드들이 이미 나갔다는 뜻

print(*answer)

