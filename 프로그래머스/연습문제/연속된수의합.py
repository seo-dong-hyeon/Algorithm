def solution(num, total):
    answer = []

    left = 1
    right = left + num - 1
    _sum = 0
    for i in range(left, right + 1):
        _sum += i

    while True:
        if _sum == total:
            break
        elif _sum > total:
            _sum -= right
            right -= 1
            left -= 1
            _sum += left
        else:
            _sum -= left
            left += 1
            right += 1
            _sum += right

    for i in range(left, right + 1):
        answer.append(i)

    return answer
