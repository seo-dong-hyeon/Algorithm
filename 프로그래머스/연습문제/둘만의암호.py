from string import ascii_lowercase

def solution(s, skip, index):
    answer = ''

    skip = [i for i in skip]
    alphabets = list(ascii_lowercase)
    next_dict = {}

    for i, alphabet in enumerate(alphabets):
        _i = i
        cnt = 0
        while cnt != index:
            _i = _i + 1 if _i + 1 != 26 else 0
            if alphabets[_i] in skip:
                continue
            cnt += 1
        next_dict[alphabet] = alphabets[_i]

    for i in s:
        answer += next_dict[i]

    return answer


print(solution("aukks",	"wbqd",	5))