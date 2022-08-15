def solution(want, number, discount):
    answer = 0
    dic_want = {}

    for i in range(len(want)):
        dic_want[want[i]] = number[i]

    for i in range(len(discount)):
        dic_discount = {}
        for j in range(10):
            if i + j >= len(discount):
                continue
            if discount[i + j] not in dic_discount:
                dic_discount[discount[i + j]] = 0
            dic_discount[discount[i + j]] += 1
        flag = True
        for key, value in dic_want.items():
            if key not in dic_discount or dic_discount[key] < value:
                flag = False
                break
        if flag:
            answer += 1

    return answer
