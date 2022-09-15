commands = []

while True:
    command = input()
    if command == "QUIT":
        break
    if command == "END":
        N = int(input())
        answers = []
        for _ in range(N):
            stack = []
            stack.append(int(input()))
            flag = False
            for command in commands:
                if command[:3] == "NUM": # 일부 문자열만 읽고 싶을 때 -> 굳이 먼저 split x -> slicing
                    stack.append(int(command.split()[1]))
                elif command == "POP" or command == "INV" or command == "DUP":
                    if len(stack) < 1:
                        flag = True
                        break
                    if command == "POP":
                        stack.pop()
                    elif command == "INV":
                        top = stack.pop()
                        stack.append(top * -1)
                    elif command == "DUP":
                        stack.append(stack[-1])
                else:
                    if len(stack) < 2:
                        flag = True
                        break
                    if command == "SWP":
                        top1 = stack.pop()
                        top2 = stack.pop()
                        stack.append(top1)
                        Vi = top2
                    elif command == "ADD":
                        Vi = stack.pop() + stack.pop()
                    elif command == "SUB":
                        top1 = stack.pop()
                        top2 = stack.pop()
                        Vi = top2 - top1
                    elif command == "MUL":
                        Vi = stack.pop() * stack.pop()
                    else:
                        divisor = stack.pop()
                        dividend = stack.pop()
                        if divisor == 0:
                            flag = True
                            break
                        if command == "DIV":
                            Vi = abs(dividend) // abs(divisor)
                            if (divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0):
                                Vi = -Vi
                        else:
                            Vi = abs(dividend) % abs(divisor) if dividend >= 0 else (abs(dividend) % abs(divisor)) * -1
                    if abs(Vi) > 1e9:
                        flag = True
                        break
                    stack.append(Vi)
            answers.append(stack[0] if len(stack) == 1 and not flag else "ERROR")
        for answer in answers:
            print(answer)
        print()
        commands = []
    elif command == "":
        continue
    else:
        commands.append(command)