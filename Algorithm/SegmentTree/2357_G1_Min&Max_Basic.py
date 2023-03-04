# 2357 / 최솟값과 최댓값[G1]
    # https://www.acmicpc.net/problem/2357

"""
    중간에 값 변경X
    범위가 주어지면, 주어진범위에서의 최소&최대 구하기
"""

import sys
input = sys.stdin.readline

    # input
n,k = map(int,input().split())

    # 세그먼트 트리 생성
        # 세그먼트 트리 최초 생성
depth = 1
while 2**depth < n:
    depth += 1
seg_min = [None]*2**(depth+1)   # 전부 None으로 초기화하기!
seg_max = [None]*2**(depth+1)       # min, max전부 걸리면 안됨
        # 세그먼트 트리 최초 원소 입력
for i in range(n):
    cur = int(input())
    seg_min[2**depth +i] = cur
    seg_max[2**depth +i] = cur
        # 세그먼트 트리 칸 채우기
cur_depth = depth-1
while cur_depth > -1:
    for i in range(2**cur_depth, 2**(cur_depth+1)):
        if seg_max[2*i] == None:    # 현재 노드의 자식이 모두 None 이면
            break                   # 뒤에도 전부 None
        elif seg_max[2*i+1] == None:    # 자식중 하나만 None이면
            seg_max[i] = seg_max[2*i]   # None아닌 값 저장
            seg_min[i] = seg_min[2*i]
            break
        else:   # 자식 모두 존재 -> 비교해서 값 선택
            seg_max[i] = max(seg_max[2*i], seg_max[2*i+1])
            seg_min[i] = min(seg_min[2*i], seg_min[2*i+1])
    cur_depth -= 1  # 더 윗칸(부모 노드)로 이동

    # 주어진 구간별 값 구하기
for _ in range(k):
    start,end = map(int,input().split())
        # 주어진 입력을 세그먼트트리 인덱스로 변경
    start_seg = 2**depth +start -1
    end_seg = 2**depth +end -1
    ans_max = seg_min[1]    # 최초값 초기화(최대값을 최소값으로)
    ans_min = seg_max[1]    # 최초값 초기화(최소값을 최대값으로)
    while start_seg <= end_seg:
        if start_seg %2 == 1:   # 조건 만족시 현재값과 비교
            if ans_max < seg_max[start_seg]:
                ans_max = seg_max[start_seg]
            if ans_min > seg_min[start_seg]:
                ans_min = seg_min[start_seg]
        if end_seg %2 == 0:   # 조건 만족시 현재값과 비교
            if ans_max < seg_max[end_seg]:
                ans_max = seg_max[end_seg]
            if ans_min > seg_min[end_seg]:
                ans_min = seg_min[end_seg]
        start_seg = (start_seg +1)//2   # 더 윗 노드로 이동
        end_seg = (end_seg -1)//2       # 더 윗 노드로 이동
    print(ans_min, ans_max) # 결과 출력
