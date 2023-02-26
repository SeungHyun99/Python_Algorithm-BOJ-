# 2637 / 장난감 조립[G2]
    # https://www.acmicpc.net/problem/2637

from collections import deque
import sys
input = sys.stdin.readline

    # input
n = int(input())    
k = int(input())    
in_deg = [0]*(n+1)  # 진입차수
order = [ [] for _ in range(n+1)]   # 하위 부품 - 현재 부품이 생성하는 부품 저장
make = [ [] for _ in range(n+1)]    # 상위 부품 - 필요한 부품과 갯수 저장
for _ in range(k):
    goal,a,cnt = map(int,input().split())
    in_deg[goal] += 1           # 진입차수
    order[a].append(goal)       # 하위 부품
    make[goal].append([a,cnt])  # 상위 부품

    # initialization
basic = []  # 기초 부품
queue = deque()
for i in range(1,n+1):
    if in_deg[i] == 0:
        queue.append(i) # Queue에 저장
        basic.append(i) # 기초부품에 저장
ans = []    # Topology Sort - 순서 저장

    # Topology Sort
while queue:
    cur = queue.popleft()
    ans.append(cur)
    for i in order[cur]:
        in_deg[i] -= 1
        if in_deg[i] == 0:
            queue.append(i)

    # Count
count = [0]*(n+1)
count[n] = 1
for i in ans[::-1]: # 완성품부터 기초부품으로 거꾸로 갯수 카운트
    for x,cnt in make[i]:
        count[x] += count[i]*cnt    # 현재부품* 필요한 하위 부품의 수 추가

for i in basic:
    print(i,count[i])
