# 2042 / 구간 합 구하기[G1]
    # https://www.acmicpc.net/problem/2042
"""
    세그먼트 트리
    누적합 + 중간중간에 값들이 변함
    INPUT a b c에서 
        a == 1 : index_b -> c
        a == 2 : index_b ~ index_c까지의 누적합 
"""

import sys
input = sys.stdin.readline

    # 값 바꿔주는 함수
def change_tree(idx_a,x):
    s_idx = idx_a + 2**l -1     # index를 세그먼트 트리의 index로 바꿔주기
    seg_tree[s_idx] = x
    s_idx //= 2
    while s_idx > 0:    # 말단노드의 부모부터 시작하여 루트노드까지 업데이트
        seg_tree[s_idx] = seg_tree[s_idx*2] + seg_tree[s_idx*2+1]
        s_idx //= 2 # 현재 노드의 부모노드로

    # 구간합을 구하는 함수
def sum_tree(idx_a, idx_b):     # 주어진 구간의 합을 구함
    result = 0  
    start = idx_a + 2**l -1
    end = idx_b + 2**l -1
    while start <= end:
        if start %2 == 1:   # start가 홀수면 result에 +
            result += seg_tree[start]
        if end %2 == 0:     # end가 짝수면 result에 +
            result += seg_tree[end]
        start = (start +1)//2   # start update
        end = (end -1)//2       # end update
    print(result)

    # input
n, num_change, num_sum = map(int,input().split())

    # 세그먼트 트리 INIT.
l = 1   # 세그먼트 트리 길이 구하기
while 2**l <n:  # 이진트리에서 리프노드(leaf node)에 각각의 값이 들어갈수 있도록 리스트 생성해주기
    l += 1
seg_tree = [0]*(2**(l+1))
for i in range(n):  # 리프노드(leaf node)에 최초의 원소들 넣어주기
    seg_tree[2**l+i] = int(input())

    # 세그먼트 트리 값 채우기
depth_start, depth_end = 2**(l-1), 2**l -1
while depth_start > 0:
    for i in range(depth_start, depth_end +1):
        seg_tree[i] = seg_tree[2*i] + seg_tree[2*i +1]  # 구하고자 하는 값에 따라 연산을 달리 하면 됨
    depth_end = depth_start -1
    depth_start //= 2

for _ in range(num_change+num_sum):
    flag,a,b = map(int,input().split())
    if flag == 1:
        change_tree(a,b)
    elif flag == 2:
        sum_tree(a,b)
