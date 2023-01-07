import sys
import copy


def calculate(op1, operator, op2):
    if operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    else:
        return op1 * op2


def go(exp, i, stack):
    # 모든 수식을 담음
    if i == len(exp):
        global answer
        result = []
        idx = 0
        while idx < len(stack):
            # 괄호 쳐진 부분은 먼저 계산
            if stack[idx] == '(':
                if len(result):
                    operator = result.pop()
                    op1 = result.pop()
                    result.append(calculate(op1, operator, calculate(stack[idx + 1], stack[idx + 2], stack[idx + 3])))
                else:
                    result.append(calculate(stack[idx + 1], stack[idx + 2], stack[idx + 3]))
                idx += 5
            # 괄호가 아니면 그냥 순차적 계산
            else:
                if stack[idx] in ['+', '-', '*']:
                    result.append(stack[idx])
                else:
                    if len(result):
                        operator = result.pop()
                        op1 = result.pop()
                        result.append(calculate(op1, operator, stack[idx]))
                    else:
                        result.append(stack[idx])
                idx += 1
        answer = max(answer, result[0])
        return
    
    # 수식이면 그냥 넣음
    if exp[i] in ['+', '-', '*']:
        stack.append(exp[i])
        go(exp, i + 1, copy.deepcopy(stack))
    else:
        # 숫자면서 앞에 '('가 있으면 숫자를 넣고 ')'로 무조건 닫아주고 다음 단계로
        if len(stack) >= 3 and stack[-3] == '(':
            stack.append(int(exp[i]))
            stack.append(')')
            go(exp, i + 1, copy.deepcopy(stack))
        else:
            # 숫자를 추가하고 다음 단계로
            # 3 + 5 * 3
            stack.append(int(exp[i]))
            go(exp, i + 1, copy.deepcopy(stack))
            # 뒤에 더 추가할 숫자들이 충분히 있다면
            # '('를 열어추고 숫자를 추가한 다음 다음 단계로
            # 3 + 5 * ( 3
            if i != len(exp) - 1:
                stack.pop()
                stack.append('(')
                stack.append(int(exp[i]))
                go(exp, i + 1, copy.deepcopy(stack))


N = int(sys.stdin.readline().rstrip())
exp = sys.stdin.readline().rstrip()
answer = 1e9 * -1

go(exp, 0, [])
print(answer)
