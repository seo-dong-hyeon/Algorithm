# 만들 수 없는 조합
import sys

N = int(sys.stdin.readline().rstrip())
coins = list(map(int, sys.stdin.readline().rstrip().split()))

coins.sort()            # 동전 오름차순 정렬
target = 1              # 만드려는 금액
for coin in coins:      # 모든 동전을 순회하며
    if coin > target:   # 동전이 금액보다 크다면 종료
        break
    target += coin      # 동전이 금액보다 작다면 타켓 금액에 동전을 더함(그 사이 금액은 다 가능하다고 판단)

print(target)