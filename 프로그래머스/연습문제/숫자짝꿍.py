def solution(X, Y):
    answer = ''
    dic_num_cnt_X = {}

    for num in X:
        num = int(num)
        if num not in dic_num_cnt_X:
            dic_num_cnt_X[num] = 0
        dic_num_cnt_X[num] += 1

    nums = []
    for num in Y:
        num = int(num)
        if num not in dic_num_cnt_X or dic_num_cnt_X[num] == 0:
            continue
        nums.append(num)
        dic_num_cnt_X[num] -= 1

    if len(nums) == 0:
        answer = '-1'
    else:
        nums.sort(reverse=True)
        for num in nums:
            answer += str(num)
        # 문자열이 하나의 문자로만 되어있는지 확인
        if answer.count('0') == len(answer):
            answer = '0'

    return answer