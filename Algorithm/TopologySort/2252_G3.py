# 2252 / 줄세우기[G3]
    # https://www.acmicpc.net/problem/2252
    # 위상정렬(TopologySort) Basic

import sys
input = sys.stdin.readline

    # ●input & initialization
n,m = map(int,input().split())
in_degree = [0]*(n+1)               # 각 정점별로 앞에 있어야 되는 정점의 수 저장
graph = [ [] for _ in range(n+1)]   # 각 정점별로 뒤에 있어야되는 정점 저장
for _ in range(m):  # 입력 받으며 진입차수(in_degree)와 graph 업데이트
    front, back = map(int,input().split())
    in_degree[back] += 1        # 뒷 노드의 진입차수 +1
    graph[front].append(back)   # 앞 노드의 graph 업데이트
case = []   # 진입차수(in_degree)가 0인 노드 저장 - 꺼내기 위해서
cnt = 0     # 꺼낸 노드 수 저장 (n이 되면 모두 꺼냈다는 뜻)
ans = []    # 꺼낸 노드 저장

    # ●위상정렬(Topologly Sort)
        # 맨 처음에 진입차수(in_degree)가 0인 노드 꺼내기
for i in range(1,n+1):
    if in_degree[i] == 0:
        case.append(i)
        
        # 한 개씩 꺼내며 진입차수 줄여주기
while cnt < n:
    cur = case.pop()    # 진입차수(in_degree)가 0인 노드 꺼내기
    ans.append(cur)     # 정답에 저장
    cnt += 1            # 꺼낸 노드 수 +1

    for i in graph[cur]:    # 현재 꺼낸 노드 뒤에 있어야 하는 노드들의 진입차수 1개씩 빼주기
        in_degree[i] -= 1
        if in_degree[i] == 0:   # 만약 이번 노드(cur)가 꺼내지면서 현재 노드(i) 앞에 있어야 하는 노드가 없다면(= indegree==0) case에 저장해주기
            case.append(i)

print(*ans)