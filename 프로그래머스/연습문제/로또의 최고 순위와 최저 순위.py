def solution(lottos, win_nums):
    answer = []

    correct = 0
    for num in lottos:
        if num in win_nums:
            correct += 1

    answer.append(min(7 - correct - lottos.count(0), 6))
    answer.append(min(7 - correct, 6))

    return answer