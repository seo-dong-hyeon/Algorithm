def solution(X, Y):
    answer = ''
    numX = [0] * 10
    numY = [0] * 10
    nums = []

    for i in range(len(X)):
        numX[int(X[i])] += 1

    for i in range(len(Y)):
        num = int(Y[i])
        if numX[num] > 0:
            nums.append(num)
            numX[num] -= 1
        
    nums.sort(reverse=True)
    if len(nums) == 0:
        answer = '-1'
    else:
        for num in nums:
            answer += str(num)
        if answer[0] == '0':
            answer = '0'

    return answer