# 끝에 0이 몇 개 = 인수로 10을 몇 개 포함
# ex), 900 = 9 x 10 x 10 = 2개
# 10 = 2 x 5 -> 10을 만들수 있는 것은 2와 5뿐
# N의 끝에 0이 몇 개 = N을 소인수분해하여 5의 배수의 개수를 구하기
# -> 5의 배수, 5x5의 배수, 5x5x5 ...의 총합
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    i = 5
    answer = 0
    while i <= N:
        answer += N // i
        i *= 5
    print(answer)
