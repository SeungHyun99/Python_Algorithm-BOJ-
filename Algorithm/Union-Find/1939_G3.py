# 1939 / 중량제한[G3]
    # https://www.acmicpc.net/problem/1939
        # 참고: https://hbj0209.tistory.com/132

from collections import deque
import sys
input = sys.stdin.readline

def find(x):    # 루트 노드 찾기
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x,y): # 두 노드 합치기
    px = find(x)
    py = find(y)
    if px<py:       # 더 숫자 낮은 부모를 루트로
        parents[py] = px
    else:
        parents[px] = py

    # input
n,m = map(int,input().split())
graph = [ ]
parents = [ i for i in range(n+1)]
for _ in range(m):
    a,b,w = map(int,input().split())
    graph.append([w,a,b])
s,e = map(int,input().split())

    # union
graph.sort(key= lambda x:-x[0]) # 두 섬 사이의 가능 중량을 내림차순으로 정렬
for i in graph:
    w,a,b = i[0], i[1], i[2]    # 두 섬과 중량 받아오기
    union(a,b)  # 두 섬 합치기
    if find(s) == find(e):  # 현재 두섬을 합쳐서 시작과 끝이 연결됐으면 현재 중량이 최대
        print(w)                    # 위에서 내림차순으로 정렬하였기 때문에
        break