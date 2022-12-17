import math

def solution(number, limit, power):
    answer = 0

    # 약수의 개수
    cnt = [0] * (number + 1)
    for i in range(1, number + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                cnt[i] += 1
                if ((j**2) != i): 
                    cnt[i] += 1

    for i in cnt:
        answer += power if i > limit else i

    return answer

print(solution(5, 3, 2))