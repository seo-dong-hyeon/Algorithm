N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

A.sort()
for num in nums:
    flag = False
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > num:
            right = mid - 1
        elif A[mid] < num:
            left = mid + 1
        else:
            flag = True
            break
    print(1 if flag else 0)