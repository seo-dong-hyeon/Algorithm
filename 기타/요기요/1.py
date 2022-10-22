# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(stack1, stack2, stack3):
    N1 = len(stack1)
    N2 = len(stack2)
    N3 = len(stack3)
    top1 = stack1[-1] if N1 != 0 else -1e9
    top2 = stack2[-1] if N2 != 0 else -1e9
    top3 = stack3[-1] if N3 != 0 else -1e9

    answer = []
    # 스택의 가장 큰 단어를 옮기기
    for _ in range(N1 + N2 + N3):
        if len(stack1) != 0 and top1 > top2 and top1 > top3:
            stack1.pop(-1)
            top1 =  stack1[-1] if len(stack1) != 0 else -1e9
            answer.append("1")
        elif len(stack2) != 0 and top2 > top1 and top2 > top3:
            stack2.pop(-1)
            top2 =  stack2[-1] if len(stack2) != 0 else -1e9
            answer.append("2")
        else:
            stack3.pop(-1)
            top3 =  stack3[-1] if len(stack3) != 0 else -1e9
            answer.append("3")
                
    return "".join(answer)



print(solution([2, 7], [4, 5], [1]))
print(solution([10, 20, 30], [8], [1]))
print(solution([7], [], [9]))