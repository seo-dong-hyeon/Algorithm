import sys

N, C = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

dict_num = {}
for i, num in enumerate(nums):
    if num not in dict_num:
        dict_num[num] = [i, 0]
    dict_num[num][1] += 1

for num, [idx, cnt] in sorted(dict_num.items(), key=lambda x:(-x[1][1], x[1][0])):
    for _ in range(cnt):
        print(num, end=' ')
print()