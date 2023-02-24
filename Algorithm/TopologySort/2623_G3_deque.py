# 2623 / 음악프로그램[G3]
    # https://www.acmicpc.net/problem/2623

    # 정석풀이 - deque를 이용

import sys
from collections import deque
input= sys.stdin.readline

    # input
n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
deg = [0]*(n+1)
for _ in range(m):
    order = list(map(int,input().split()))
    for i in range(1,order[0]):
        graph[order[i]].append(order[i+1])  # 앞뒤 노드의 순서를 저장
        deg[order[i+1]] +=1 # 뒷노드의 in_degree +1

    # initialization
q = deque([])
for i in range(1,n+1):
    if deg[i]==0:
        q.append(i)
result = []

    # Topology Sort
while q:
    cur = q.popleft()
    result.append(cur)
    for nxt in graph[cur]:
        deg[nxt] -= 1
        if deg[nxt] == 0:
            q.append(nxt)

    # Answer
if len(result) ==n: # 모든 노드가 정렬 가능
    print(*result,sep="\n")
else: print(0)      #  모든 노드가 순서에 맞게 정렬 불가능