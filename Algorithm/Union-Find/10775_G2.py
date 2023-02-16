# 10775 / 공항[G2]
    # https://www.acmicpc.net/problem/10775

'''
    § Union-Find의 활용 방법(Idea)
    1. 그리디하게 현재 비행기를 넣을 수 있는 최대 번호에 주차
    2. 주차후 현재 주차 구역과 바로 앞을 union하여 이미 주차된곳에 주차되지 않도록 함
    EX) 4대가 연속으로 3 3 3 3이 들어온다고 가정
        1번째 비행기: 3 주차 // 3과 2(=3-1)이 union
        2          : 2 주차 (현재 find(3) = 2) // 2와 1(=2-1)이 union  
        3          : 1 주차 (현재 find(3) = 1) // 1와 0(=1-1)이 union 
        4          : 주차불가 (현재 find(3) = 0) // 더이상 주차 불가 >> flag = False
'''

import sys
input = sys.stdin.readline

def find(x):
    if lst_max[x] == x:
        return x
    else:
        lst_max[x] = find(lst_max[x])
        return lst_max[x]

def union(x,y):
    px = find(x)
    py = find(y)
    if px<py:
        lst_max[py] = px
    else:
        lst_max[px] = py


    # input
g = int(input())    # 총 Gate 수
p = int(input())    # 총 비행기 수
lst_max = [ i for i in range(g+1)]  # 각 게이트내에서 주차할 수 있는 최대 Gate 넘버
flag = True # 공항 폐쇄 여부
cnt = 0 # 주차 비행기 수
    # 주차
for _ in range(p):
    cur = int(input())  # Gate 받기
    if flag == False:       # 공항 폐쇄 이후
        continue

    elif find(cur) == 0:    # 더이상 공항에 주차 불가
        flag = False            # >>> cur이내의 주차장이 이미 만차
        continue                # 공항 폐쇄
    else:                   # 주차 가능
        cnt += 1                # 주차 비행기 +1
        union(find(cur),find(cur)-1)    # 현재 주차한 곳과 앞 곳을 union

print(cnt)  # ANS 출력