# 1725 / 히스토그램[P5]
    # https://www.acmicpc.net/problem/1725

"""
    문제 요약: 주어진 히스토그램에 속하는 가장 넓은 직사각형의 넓이를 구하시오

    ※ 해당 문제를 푸는 방식은 2가지가 존재 - 분할 정복 / 스택
        >> 그중에서 분할 정복 방식    
    
    ※ 논리: 
        1. 주어진 구간의 밑변으로 하는 직사각형의 넓이를 구한다.
            >> 주어진 구간에서의 최소높이와 그 위치를 찾는다.
        2. 구한 최소 위치를 기준으로 좌,우를 나눈다.
        3. 1번을 반복한다.

    ※ 6549번 - 히스토그램에서 가장 큰 직사각형 문제와 똑같은 문제
        6549번 문제: 한 문제에서 현재 문제가 여러개가 들어가 있음.

    ※ 참고: https://www.acmicpc.net/blog/view/12
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

    # 주어진 두 구간에서의 최소값을 구함 - segment tree
def find_min(idx_a, idx_b):     # 0 <= idx_a, idx_b < n
        # init
    start = 2**depth + idx_a        #  └> index 시작을 0부터 함
    end = 2**depth + idx_b
    res = idx_a                 # 가장 낮은 높이를 갖는 위치(index)
    res_value = height[idx_a]   # 가장 낮은 높이
        # segment tree
    while start <= end:
        if start %2 == 1:
            cur = height[seg[start]]    # 현재 index(start)에서의 높이
            if cur < res_value:     # 더 작을 경우 값 업데이트
                res = seg[start]
                res_value = cur
        if end %2 == 0:
            cur = height[seg[end]]      # # 현재 index(end)에서의 높이
            if cur < res_value:     # 더 작을 경우 값 업데이트
                res = seg[end]
                res_value = cur
        start = (start +1)//2
        end = (end -1)//2

    return (res_value, res) # 최저 높이와 그 인덱스를 return
        
    # 분할 정복을 활용하여 넓이 구하기
def get_area(left, right):
    global max_area
    if left > right:    # 좌측이 우측보다 큰값을 가질 경우 종료
        return
    min_value, min_idx = find_min(left,right)   # 현재 구간에서의 최소값과 위치 구하기
    if min_value*(right -left +1) > max_area:       # 만약 현재 구간에서의 최대 직사각형의 넓이가 기존 최대값보다 클 경우
        max_area = min_value*(right -left +1)

    get_area(left, min_idx -1)      # 가장 낮은 위치 기준 좌측에 대해 get_area 함수 분할 정복 실시
    get_area(min_idx +1, right)     #                    우측에 대해 실시


    # input
n = int(input())
depth = 1
while 2**depth < n: # segment tree 깊이(크기) 구하기
    depth += 1
seg = [None]*2**(depth+1)
seg[2**depth : 2**depth +n] = [i for i in range(n)]     # segment tree에 각각의 위치(height리스트의 index)를 저장함(0~n-1)
height = []
for _ in range(n):
    height.append(int(input()))

    # segment tree 값 채우기
cur_depth = depth -1
while cur_depth >= 0:
    for i in range(2**cur_depth, 2*2**cur_depth):
        child_left = 2*i
        child_right = 2*i +1
        if seg[child_left] == None:
            break
        elif seg[child_right] == None:
            seg[i] = seg[child_left]
            break
        else:
            value_left = height[seg[child_left]]    # 좌측 새끼노드의 높이
            value_right = height[seg[child_right]]  # 우측 새끼노드의 높이
            if value_left < value_right:    # 더 낮은 새끼노드르 저장
                seg[i] = seg[child_left]        # 이 역시, 더 낮은 위치의 index (height에서의 index)
            else:
                seg[i] = seg[child_right]
    cur_depth -= 1  # 다음 depth로

    # solve
max_area = 0
get_area(0,n-1)
print(max_area)
