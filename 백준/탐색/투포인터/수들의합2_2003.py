N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

left = 0
right = 0
sum = nums[0]

while True:
    if sum > M:
        sum -= nums[left]
        left += 1
        if left >= N:
            break
        if left > right:
            right = left
            sum = nums[right]
    else:
        if sum == M:
            answer += 1
        right += 1
        if right < N:
            sum += nums[right]
        else:
            sum -= nums[left]
            left += 1
            if left >= N:
                break

print(answer)