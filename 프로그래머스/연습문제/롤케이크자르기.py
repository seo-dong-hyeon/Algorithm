def solution(topping):
    answer = 0
    dic_left = {}
    left = set()
    dic_right = {}
    right = set()

    dic_left[topping[0]] = 1
    left.add(topping[0])
    for i in range(1, len(topping)):
        if topping[i] not in dic_right:
            dic_right[topping[i]] = 0
        dic_right[topping[i]] += 1
        right.add(topping[i])

    for i in range(1, len(topping)):
        if len(left) == len(right):
            answer += 1
        if topping[i] not in dic_left:
            dic_left[topping[i]] = 0
        dic_left[topping[i]] += 1
        left.add(topping[i])
        dic_right[topping[i]] -= 1
        if dic_right[topping[i]] == 0:
            right.remove(topping[i])

    return answer
