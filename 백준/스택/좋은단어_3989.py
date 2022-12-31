# 괄호 짝짓기 문제
# 만약 선끼리 교차하지 않으면서 
# 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝 지을수 있다면
# 스택 문제
import sys 

N = int(sys.stdin.readline().rstrip())
answer = 0

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    stack = []
    for w in word:
        if len(stack) == 0:
            stack.append(w)
        else:
            if stack[-1] == w:
                stack.pop()
            else:
                stack.append(w)
    if len(stack) == 0:
        answer += 1

print(answer)