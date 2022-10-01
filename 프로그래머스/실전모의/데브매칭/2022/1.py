def solution(registered_list, new_id):
    answer = ''

    # 단어 사전
    dict_registered = {}
    for i in range(len(registered_list)):
        dict_registered[registered_list[i]] = True

    while True:
        # 단어 사전에 없으면 리턴
        if new_id not in dict_registered:
            return new_id
        # 최초의 숫자 등장 인덱스 찾기
        digitIdx = -1
        for i in range(len(new_id)):
            if new_id[i].isdigit():
                digitIdx = i
                break
        # 숫자인 문자가 없다면 0을 붙임
        if digitIdx == -1:
            S = new_id
            N = "0"
        # 문자열을 문자, 숫자 형태로 분리
        # 숫자를 1 증가하여 새로운 문자열
        else:
            S = new_id[:i]
            N = new_id[i:]
        N = str(int(N) + 1)
        new_id = S + N

    return answer

# print(solution(["cow", "cow1", "cow2"], "cow"))   # cow3