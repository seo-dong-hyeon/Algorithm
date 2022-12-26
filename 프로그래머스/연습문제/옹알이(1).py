def is_bab(words, s):
    before = []

    while s:
        flag = False
        for word in words:
            if word not in before and word == s[:len(word)]:
                before.append(word)
                flag = True
                s = s[len(word):]
        if not flag:
            return False

    return True


def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]

    for i in range(len(babbling)):
        if is_bab(words, babbling[i]):
            answer += 1

    return answer
    