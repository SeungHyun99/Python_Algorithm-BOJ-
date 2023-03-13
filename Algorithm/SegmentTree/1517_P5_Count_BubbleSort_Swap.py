# 1517 / 버블 소트[P5]
    # https://www.acmicpc.net/problem/1517

"""
    문제: 버블 소트를 수행할 때 발생하는 swap횟수를 구하시오
    *논리: 
        각 숫자들의 swap횟수 = 본인보다 앞에 있는 숫자들 중 본인들보다 더 큰 수
        1. 먼저, 최종 sort된 리스트를 구한 후, 각 숫자들과 순서를 mapping 해준다
            ex) 12/12/34/56 >> 12: 1 / 34: 2 / 56: 3
        2. 리스트의 앞원소부터 본인보다 먼저 나온 더 큰수의 갯수를 구한다
            >> 세그먼트 트리 누적함
        3. 본인 순서에 +1해주고 세그먼트 트리를 업데이트해준다.
        *최종 트리의 리프노드에 있는 숫자들은 해당 숫자의 갯수이다.
            ex) 12/12/34/56 >>  1(원래 숫자=12): 2 
                                2(원래 숫자=34): 1
                                3(원래 숫자=56): 1
"""


import sys
input=sys.stdin.readline

def find(num_a, num_b):
    start = size + num_a -1
    end = size + num_b -1
    res = 0
    while start <= end:
        if start %2 == 1:
            res += seg[start]
        if end %2 == 0:
            res += seg[end]
        start = (start+1)//2
        end = (end -1)//2
    return res

def update(node):
    temp=size+node-1
    while temp>=1:
        seg[temp]+=1
        temp//=2

    # $input
n=int(input())
nums=list(map(int,input().split()))

    # $각 숫자들과 최종 위치를 mapping
temp = nums[:]  # 각 숫자들의 최종 위치를 확인해주기 위한 리스트
temp.sort()     # 정렬 - 최종 결과
order = {}      # 각 숫자들의 순서를 저장
mapping_num = 1
for i in temp:
    if order.get(i,-1) == -1:       # 123 / 123 / 456 / 789 이렇게 있다면
        order[i] = mapping_num      # 123에는 1부여, 456에는 2부여
        mapping_num += 1            # 789에는 3부여

    # $세그먼트 트리 크기 구하기
depth = 1
while 2**depth < n:
    depth += 1
size=2**depth
seg=[0]*(size*2)

    # $앞에서부터 필요한 swap 횟수 구하기
ans=0
for i in nums:
    cur_idx = order[i]          # 현재 숫자의 최종 위치 구학
    ans += find(cur_idx +1,n)   # 현재까지 나온 수들중에서 더 큰수가 나온 횟수 구하기 - 세그먼트트리 누적합
    update(cur_idx)             # 현재 위치에 +1을 하고 세그먼트 트리 업데이트
print(ans)