import sys

while True:
    try:
        S = sys.stdin.readline().rstrip()
        if len(S) == 1 and S[0] == '.':
            break
        flag = True
        stack = []
        for i in range(len(S)):
            if S[i] == '(' or S[i] == '[':
                stack.append(S[i])
            elif S[i] == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    flag = False
                    break
                stack.pop()
            elif S[i] == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    flag = False
                    break
                stack.pop()
        if len(stack):
            flag = False
        print("yes" if flag else "no")
    except:
        break