import sys
from string import ascii_lowercase 

message = sys.stdin.readline().rstrip()
key = sys.stdin.readline().rstrip()
maze = [[''] * 5 for _ in range(5)]
poses = {}
dict_alpha = {}

for alpha in list(ascii_lowercase):
    if alpha == 'j':
        continue
    dict_alpha[alpha.upper()] = False

# 표 만들기
keyIdx = 0
i = 0
j = 0
while True:
    # key 문자열은 전부 채웠으면
    # 아직 등장하지 않은 문자를 표에 넣음
    if keyIdx >= len(key):
        for alpha, checked in dict_alpha.items():
            if checked == False:
                dict_alpha[alpha] = True
                maze[i][j] = alpha
                poses[maze[i][j]] = [i, j]
                break
    else:
        # 해당 key 문자가 이미 나온적 있으면 다음 문자로
        if dict_alpha[key[keyIdx]] == True:
            keyIdx += 1
            continue
        # 해당 key 문자가 나온적 없으면 표에 넣음
        else:
            maze[i][j] = key[keyIdx]
            dict_alpha[key[keyIdx]] = True
            poses[maze[i][j]] = [i, j]
    keyIdx += 1
    j += 1
    if j == 5:
        j = 0
        i += 1
    if i == 5 and j == 0:
        break

# 두 글자씩 나누기
converted = ''
while True:
    flag = True
    converted = ''  # 변환된 문자열
    for i in range(0, len(message), 2):
        # 마지막 문자면 추가 후 종료
        if i + 1 >= len(message):
            converted += message[i]
            break
        w1, w2 = message[i], message[i + 1]
        # 연속된 문자열이면
        # 가운데 X나 Q 추가 후 
        # 이후의 문자열들도 추가 후 다시 시작
        if w1 == w2:
            converted += w1
            converted += 'X' if w1 != 'X' else 'Q'
            converted += message[i + 1:]
            flag = False
            break
        # 연속되지 않은 문자열이면
        # 단순히 이어붙임
        else:
            converted += w1
            converted += w2   
    # 전부 이어붙임 
    if flag:
        break
    message = converted

# 끝에 문자열이 남아있으면 X 추가
message = ''.join(converted)
if len(message) % 2 != 0:
    message += 'X'

# 변환
answer = ''
for i in range(0, len(message), 2):
    x1, y1 = poses[message[i]]
    x2, y2 = poses[message[i + 1]]
    if x1 == x2:    # 행이 같을 때
        answer += maze[x1][y1 + 1 if y1 + 1 < 5 else 0] 
        answer += maze[x2][y2 + 1 if y2 + 1 < 5 else 0] 
    elif y1 == y2:  # 열이 같을 때
        answer += maze[x1 + 1 if x1 + 1 < 5 else 0][y1] 
        answer += maze[x2 + 1 if x2 + 1 < 5 else 0][y2] 
    else:           # 둘 다 다를 때
        answer += maze[x1][y2]
        answer += maze[x2][y1]

print(answer)
