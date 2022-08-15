# 스택, 큐에서 뽑기 문제 
# while 문으로 조건에 맞을 때까지 계속 뽑는 경우 고려

def solution(order):
    answer = 0
    stack = []
    orderIdx = 0    # 뽑아야 할 순서 번호

    for i in range(len(order)):
        num = i + 1
        if num == order[orderIdx]:  # 현재 컨테니어 상자가 실어야 할 상자면 바로 실음
            answer += 1
            orderIdx += 1
            continue
        if len(stack):  # 보조 컨테이너에 상자가 있다면
            while len(stack):   # 뽑아야 할 순서가 맞을 때까지 보조 컨테이너에서 뽑음
                if stack[-1] == order[orderIdx]:
                    stack.pop(-1)
                    answer += 1
                    orderIdx += 1
                else:
                    break
            if num == order[orderIdx]:  # 현재 컨테니어 상자가 실어야 할 상자면 바로 실음
                answer += 1
                orderIdx += 1
            else:   # 아니라면 보조 컨테이너에 실음
                stack.append(num)
        else:   # 보조 컨테이너에 상자가 없다면 바로 실어버림
            stack.append(num)

    if len(stack):  # 보조 컨테이너에 상자가 있다면
        while len(stack):   # 뽑아야 할 순서가 맞을 때까지 보조 컨테이너에서 뽑음
            if stack[-1] == order[orderIdx]:
                stack.pop(-1)
                answer += 1
                orderIdx += 1
            else:
                break

    return answer
