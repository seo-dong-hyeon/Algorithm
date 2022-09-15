# 똑똑한 그리디
# 단어 수학 문제
# dfs, 순열조합 X
# 앞에부터 많이 나온 단어일수록 높은 점수
# 전체 빈도만 구하면 됨
# 단어의 순위를 정하고 높은 순위부터 숫자부여
# ex) ABAC -> A=1010 > B=100 > C=1 -> A = 9, B = 8, C = 7
N = int(input())
words = []
dict_alpha_digit = {}
dict_alpha_num = {}
answer = 0

# 단어의 빈도를 구함
# 내림차순 정렬
for _ in range(N):
    word = input()
    words.append(word)
    word = word[::-1]
    digit = 1
    for w in word:
        dict_alpha_digit.setdefault(w, 0)
        dict_alpha_digit[w] += digit
        digit *= 10
dict_alpha_digit = sorted(dict_alpha_digit.items(), key=lambda x: -x[1])

# 단어의 순위에 따라 숫자부여
num = 9
for key, value in dict_alpha_digit:
    dict_alpha_num[key] = num
    num -= 1

# 주어진 단어에 대해 정해진 숫자로 계산
for word in words:
    word2Num = ""
    for w in word:
        word2Num += str(dict_alpha_num[w])
    answer += int(word2Num)

print(answer)