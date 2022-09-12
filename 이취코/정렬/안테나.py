# 일직선상에서 모든 집으로부터 
# 거리의 합이 최소가 되는 위치
# 모든 집들 상의 가운데 위치
# 가운데 위치 -> arr[(len(arr) - 1) // 2]
# 예시
# 1(집) 2 3 4 5(집) 6 7(집) 8 9(집)
# arr = [1, 5, 7, 9]
# arr[(4 - 1) // 2] = 5
import sys

N = int(sys.stdin.readline().rstrip())
houses = list(map(int, sys.stdin.readline().rstrip().split()))

houses.sort()

print(houses[(len(houses) - 1) // 2])

# 가운데 1칸 왼쪽, 가운데, 가운데 1칸 오른쪽 비교
# if len(houses) <= 2:
#     print(houses[0])
# else:
#     antenna1 = houses[int(len(houses) / 2) - 1]
#     antenna2 = houses[int(len(houses) / 2)]
#     antenna3 = houses[int(len(houses) / 2) + 1]
#     diff1 = 0
#     diff2 = 0
#     diff3 = 0
#     for house in houses:
#         diff1 += abs(antenna1 - house)
#         diff2 += abs(antenna2 - house)
#         diff3 += abs(antenna2 - house)
#     minDiff = min(diff1, diff2, diff3)
#     if minDiff == diff1:
#         print(antenna1)
#     elif minDiff == diff2:
#         print(antenna2)
#     else:
#         print(antenna3)