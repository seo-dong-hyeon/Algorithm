# 투포인터 - 부분합
# 최초 부분합 - 리스트 첫번째 값
# 부분합이 구하려는 값보다 크면 왼쪽 인덱스를 이동 후 부분합 갱신
# 부분합이 구하려는 값보다 작으면 오른쪽 인덱스를 이동 후 부분합 갱신
N, S = map(int, input().split())
nums = list(map(int, input().split()))
answer = 1e9

left = 0
right = 0
sum = nums[0]
while True:
    if sum >= S:
        answer = min(answer, right - left + 1)
        sum -= nums[left]
        left += 1
        if left >= N:
            break
        if left > right:
            right = left
            sum = nums[right]
    else:
        right += 1
        if right < N:
            sum += nums[right]
        else:
            sum -= nums[left]
            left += 1
            if left >= N:
                break

print(answer if answer != 1e9 else 0)