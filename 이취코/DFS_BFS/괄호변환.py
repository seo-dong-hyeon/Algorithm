# 올바른 괄호 문자열 검사
def isCorrect(w):
    stack = []
    for i in range(len(w)):
        if w[i] == '(':
            stack.append(w[i])
        else:
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop(-1)
    
    if len(stack) != 0:
        return False
    return True


def makeCorrectStr(w):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if len(w) == 0:
        return w
    cnt1 = 0
    cnt2 = 0
    u = ''
    v = ''
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    for i in range(len(w)):
        if w[i] == '(':
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 == cnt2:
            u = w[:i + 1]
            v = w[i + 1:]
            break
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    if isCorrect(u):
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        return u + makeCorrectStr(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        # 4-3. ')'를 다시 붙입니다. 
        newStr = '(' + makeCorrectStr(v) + ')'
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == '(':
                newStr += ')'
            else:
                newStr += '('
        # 4-5. 생성된 문자열을 반환합니다.
        return newStr

def solution(p):
    answer = makeCorrectStr(p)
    return answer