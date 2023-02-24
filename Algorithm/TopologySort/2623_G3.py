# 2623 / 음악프로그램[G3]
    # https://www.acmicpc.net/problem/2623

import sys
input = sys.stdin.readline

    # input
n,k = map(int,input().split())
deg = [0]*(n+1) # 앞에 있어야 하는 노드의 수
graph = [ [] for _ in range(n+1)]   # 뒤에 있어야 하는 노드
for _ in range(k):
    count, *order = map(int,input().split())
    for i in range(count-1):
        front, back = order[i], order[i+1]
        graph[front].append(back)   # graph 업데이트
        deg[back] += 1              # deg 업데이트
cnt = 0
ans = []

    # 위상정렬
while cnt < n:  # n개의 노드가 정렬될때까지
    flag = True     # 정렬가능한 노드가 없음: True / 있음: False
    for x in range(1,n+1):  # 1번부터 돌아가며 deg==0 확인
        if deg[x] == 0: # 앞에 있어야하는 노드X >> 정렬(이미 정렬된 노드는 -1이 됨)
            flag = False
            ans.append(x)
            cnt += 1    # 정렬된 노드 수 +1
            deg[x] -= 1 # 정렬된 노드의 deg = -1
            for i in graph[x]:  # 현재 노드가 줄어들며 이 노드 뒤의 와야하는 노드들의 deg -1
                deg[i] -= 1

    if flag:    # 만약 flag == True: 이번에 정렬된 노드가 없다는 듯
        ans = [0]
        break

    # 결과 출력
print(*ans,sep='\n')