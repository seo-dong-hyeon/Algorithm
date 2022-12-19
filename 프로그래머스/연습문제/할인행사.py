from collections import deque

def check(want, number, dic_discount):
    flag = True

    for i in range(len(want)):
        if want[i] not in dic_discount or dic_discount[want[i]] < number[i]:
            flag = False
            break
    
    return flag


def solution(want, number, discount):
    answer = 0

    # 원하는 상품 수
    dic_want = {}
    for i in range(len(want)):
        dic_want[want[i]] = number[i]

    # 초기 10개 할인 상품 항목 및 수
    dq = deque()
    dic_discount = {}
    for i in range(10):
        if discount[i] not in dic_discount:
            dic_discount[discount[i]] = 0
        dic_discount[discount[i]] += 1
        dq.append(discount[i])

    # 10일째부터 마지막 날까지
    for i in range(10, len(discount)):
        # 현재 할인 상품 항목 수가 원하는 상품 수를 충족하는지 확인
        if check(want, number, dic_discount):
            answer += 1

        # 가장 오래전 할인 상품 항목의 수 감소
        # 현재 할인 상품 항목의 수 증가
        dic_discount[dq.popleft()] -= 1
        if discount[i] not in dic_discount:
            dic_discount[discount[i]] = 0
        dic_discount[discount[i]] += 1

        # 현재 할인 상품 항목 할인 추가
        dq.append(discount[i])

    # 마지막 날에 추가된 할인 상품 항목 추가하여
    # 현재 할인 상품 항목 수가 원하는 상품 수를 충족하는지 확인
    if check(want, number, dic_discount):
        answer += 1

    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))