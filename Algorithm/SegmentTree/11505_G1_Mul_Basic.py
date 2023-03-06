# 11505 / 구간 곱 구하기[G1]
    # https://www.acmicpc.net/problem/11505

"""
    원소들이 주어지고 경우에 따라 값을 변경하거나 구간의 곱을 구함
    구간의 곱 출력시 1,000,000,007로 나눈 나머지를 출력
"""

import sys
input = sys.stdin.readline

    # idx_a의 원소를 x로 바꾸는 함수
def change(idx_a,x):    
    idx_seg_a = 2**depth +idx_a -1  # idx_a의 세그먼트 트리에서의 idx 구하기
    seg_mul[idx_seg_a] = x
    cur_idx = idx_seg_a //2
    while cur_idx > 0:  # 계속 부모노드로 올라가서 최종 루트 노드까지 값 업데이트
        if seg_mul[2*cur_idx+1] == None:
            seg_mul[cur_idx] = seg_mul[2*cur_idx]
        else:
            seg_mul[cur_idx] = (seg_mul[2*cur_idx] * seg_mul[2*cur_idx +1])%criterion
        cur_idx //= 2       # 부모 노드로 이동

    # idx_a ~ idx_b까지의 곱
def mul(idx_a, idx_b):   
    start = 2**depth +idx_a -1  # 시작점 - idx_a의 세그먼트 트리에서의 인덱스
    end = 2**depth +idx_b -1    # 종료점 - idx_b의 세그먼트 트리에서의 인덱스
    res = 1
    while start <= end:
        if start %2 == 1:   # 시작점이 홀수 >> 값(res)업데이트
            res *= seg_mul[start]
            res %= criterion
        if end %2 == 0:     # 종료점이 짝수 >> 값(res)업데이트
            res *= seg_mul[end]
            res %= criterion
        if res == 0:        # 더 이상의 곱셈이 의미가 없음
            break
        start = (start+1)//2    # 더 상단의 노드로 이동
        end = (end-1)//2
    print(res)

    # input
n,cnt_change,cnt_mul = map(int,input().split()) 
    # 세그먼트 트리의 크기(depth)구하기
depth = 1
while 2**depth < n:
    depth += 1
seg_mul = [None]*2**(depth+1)   # 전부 None으로 초기화(곱셈의 경우 1로 초기화해도 상관X)
for i in range(n):
    cur_idx = 2**depth + i
    seg_mul[cur_idx] = int(input())

    # 세그먼트 트리 값 채우기
criterion = 1000000007  # mod 기준값
cur_depth = depth -1
while cur_depth >= 0:       # 루트노드까지
    for i in range(2**cur_depth,2*2**cur_depth):
        if seg_mul[2*i] == None:    # 왼쪽 자식이 None
            break
        elif seg_mul[2*i+1] == None:# 오른쪽 자식이 None
            seg_mul[i] = seg_mul[2*i]
            break
        else:
            seg_mul[i] = (seg_mul[2*i]*seg_mul[2*i+1])%criterion
    cur_depth -= 1  # 더 윗칸으로 이동

for _ in range(cnt_mul + cnt_change):
    flag,a,b = map(int,input().split())
    if flag == 1:
        change(a,b)
    else:
        mul(a,b)