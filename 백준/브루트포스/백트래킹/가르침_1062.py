# 백트래킹
# 시작 범위 제한 -> 전체 범위를 탐색을 하되, 처음 시작 index 조절
import sys
from string import ascii_lowercase

N, K = map(int, sys.stdin.readline().rstrip().split())
alphabets = list(ascii_lowercase)
words = []
answer = 0

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    word = word.replace("anta","").replace("tica","")
    words.append(word)

checked = {}
for alphabet in alphabets:
    checked[alphabet] = False
checked['a'] = True
checked['n'] = True
checked['t'] = True
checked['i'] = True
checked['c'] = True

def dfs(idx, readCnt):
    global K
    global answer
    if readCnt == K:
        learnCnt = 0
        for word in words:
            flag = True
            for w in word:
                if checked[w] == False:
                    flag = False
                    break
            if flag:
                learnCnt += 1
        answer = max(answer, learnCnt)
        return

    for i in range(idx, len(checked)):      # idx부터 시작
        if checked[alphabets[i]] == False:
            checked[alphabets[i]] = True    # 체크 표시
            dfs(i, readCnt + 1)             # 다음 단계로
            checked[alphabets[i]] = False   # 체크 표시 해제

K -= 5
if K < 0:
    print(0)
elif K == 21:
    print(N)
else:
    dfs(0, 0)
    print(answer)