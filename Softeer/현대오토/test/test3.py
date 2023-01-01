'''
그리디 알고리즘(최대 증가 구간 = 재귀적으로 계속 돌면서 현재보다 큰 값들만 찾아다님)

p = [103,101,103,103,101,102,100,100,101,104] 일때

1.p를 오름차 순으로 정렬
p = [100,100,101,101,101,102,103,103,103,104]

2.p와 같은 길이의 check 리스트를 만듦
chkList = [False,False,False,False,False,False,False,False,False,False]

3.p리스트 탐색

4.p값중에 chkList[index]값이 False(아직 체크 안한 값)면서 현재 p값보다 큰 곳으로 이동

5.이동할 때마다 chkList[index]값을 True로 변경, answer 값에 1을 더함

6.3 ~ 5번 과정 반복

예시)
현재 index = 0, answer = 0
p = [100, 100, 101, 101, 101, 102, 103, 103, 103, 104]
c = [ X ,  X,   X,   X,   X,   X,   X,   X,   X,   X ]
      ^

현재 index = 2, answer = 1
p = [100, 100, 101, 101, 101, 102, 103, 103, 103, 104]
c = [ O ,  X,   X,   X,   X,   X,   X,   X,   X,   X ]
                ^

현재 index = 5, answer = 2
p = [100, 100, 101, 101, 101, 102, 103, 103, 103, 104]
c = [ O ,  X,   O,   X,   X,   X,   X,   X,   X,   X ]
                               ^

현재 index = 6, answer = 3
p = [100, 100, 101, 101, 101, 102, 103, 103, 103, 104]
c = [ O ,  X,   O,   X,   X,   O,   X,   X,   X,   X ]
                                    ^                

현재 index = 9, answer = 4
p = [100, 100, 101, 101, 101, 102, 103, 103, 103, 104]
c = [ O ,  X,   O,   X,   X,   O,   O,   X,   X,   X ]
                                                   ^
                                                          
현재 index = 1, answer = 4
p = [100, 100, 101, 101, 101, 102, 103, 103, 103, 104]
c = [ O ,  X,   O,   X,   X,   O,   O,   X,   X,   O ]
           ^

현재 index = 3, answer = 5
p = [100, 100, 101, 101, 101, 102, 103, 103, 103, 104]
c = [ O ,  O,   O,   X,   X,   O,   O,   X,   X,   O ]
                     ^

현재 index = 7, answer = 6
p = [100, 100, 101, 101, 101, 102, 103, 103, 103, 104]
c = [ O ,  O,   O,   O,   X,   O,   O,   X,   X,   O ]
                                         ^

현재 index = 4, answer = 6
p = [100, 100, 101, 101, 101, 102, 103, 103, 103, 104]
c = [ O ,  O,   O,   O,   X,   O,   O,   O,   X,   O ]
                          ^        

현재 index = 8, answer = 7
p = [100, 100, 101, 101, 101, 102, 103, 103, 103, 104]
c = [ O ,  O,   O,   O,   O,   O,   O,   O,   X,   O ]
                                              ^        

모든 값 check -> answer = 7 = 최대 증가 구간       
'''

def recursive(p, idx, num, chkList, answer):
    for idx in range(len(p)):
        if chkList[idx] == False and p[idx] > num:
            chkList[idx] = True
            answer += recursive(p, idx, p[idx], chkList, answer)
            return answer + 1
    return answer


def solution(p):
    answer = 0
    p.sort()
    chkList = [False] * len(p)

    for i in range(len(p)):
        if chkList[i] == False:
            chkList[i] = True
            answer += recursive(p, i, p[i], chkList, 0)

    return answer