def solution(inp_str):
    answer = [] # 위배된 규칙 번호
    # charKinds = 문자 종류 등장 여부
    # 'A' ~ 'Z' 등장 -> charKinds[0] = True
    # 'a' ~ 'z' 등장 -> charKinds[1] = True
    # '0' ~ '9' 등장 -> charKinds[2] = True
    # 특수문자 등장 -> charKinds[3] = True
    charKinds = [False,False,False,False]
    specialChar = ['~','!','@','#','$','%','^','&','*']
    pastChar = "" # 이전 문자 저장
    repeat = 1 # 문자의 반복횟수

    # 1번 규칙 검사 - 문자열 길이가 8보다 작거나 15보다 크면 1 저장
    length = len(inp_str)
    if length < 8 or length > 15:
        answer.append(1)
    
    # 모든 문자열을 탐색하면서
    for i in range(len(inp_str)):
        if pastChar == inp_str[i]: # 이전 문자가 현재 문자와 같으면
            repeat += 1 # 반복횟수 증가
        else: # 이전 문자가 현재 문자와 다르면
            repeat = 1 # 반복횟수는 1로 초기화
        pastChar = inp_str[i] # 이전 문자 = 현재 탐색하는 문자

        # 4번 규칙 검사 - 문자의 반복횟수가 4번 이상이면 4 저장
        if repeat >= 4:
            answer.append(4)

        # 2번 규칙 검사 - 지정된 문자이외의 문자가 있다면 2 저장
        if (inp_str[i] >= 'A' and inp_str[i] <= 'Z'):
            charKinds[0] = True
        elif (inp_str[i] >= 'a' and inp_str[i] <= 'z'):
            charKinds[1] = True
        elif (inp_str[i] >= '0' and inp_str[i] <= '9'):
            charKinds[2] = True
        elif (inp_str[i] in specialChar):
            charKinds[3] = True
        else: # 지정된 문자 이외의 문자
            answer.append(2) # 2 저장

    # 3번 규칙 검사 - 문자 종류가 3개 미만이면 3 저장
    if charKinds.count(True) < 3:
        answer.append(3)

    # 5번 규칙 검사 - 모든 문자에 대해 문자열에서 등장횟수가 5번 이상이면 5 저장
    for i in range(len(inp_str)):
        c = inp_str[i]
        if inp_str.count(c) >= 5:
            answer.append(5)
            break

    if len(answer) == 0: # 어떤 규칙도 위배x
        answer.append(0) # 0 저장
    else: # 위배한 규칙이 있다면
        answer = list(set(answer)) # 중복된 값을 제거

    return answer