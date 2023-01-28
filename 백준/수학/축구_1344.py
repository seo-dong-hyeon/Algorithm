import sys
import math

def get_primes(n):
    array = [True for _ in range(n + 1)] 
    array[0] = False
    array[1] = False

    for i in range(2, int(math.sqrt(n)) + 1): 
        if array[i] == True: 
            j = 2 
            while i * j <= n:
                array[i * j] = False
                j += 1

    return array


def get_nCr(n, r):
    return int(math.factorial(n) / (math.factorial(n - r) * math.factorial(r)))


prob_A = int(sys.stdin.readline().rstrip()) / 100
prob_B = int(sys.stdin.readline().rstrip()) / 100
N = 18
primes = get_primes(N)

# A, B가 소수 아닌 개수의 골을 넣을 확률의 합 계산
sum_prob_A = 0.0
sum_prob_B = 0.0
for score in range(N + 1):
    if primes[score] is False:
        sum_prob_A += get_nCr(N, score) * math.pow(prob_A, score) * math.pow(1 - prob_A, N - score)
        sum_prob_B += get_nCr(N, score) * math.pow(prob_B, score) * math.pow(1 - prob_B, N - score)

# 전체 확률에서 소수 아닌 개수의 골 넣을 확률을 뺌
# = 적어도 1팀은 소수 개수의 골을 넣은 확률
answer = 1.0 - sum_prob_A * sum_prob_B
print(answer)
