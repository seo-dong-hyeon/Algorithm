def solution(s):
    answer = len(s)
    total_length = len(s)

    for length in range(1, total_length // 2 + 1):
        i = 0
        base = s[i:length]
        compressed = ""
        cnt = 0
        while i < len(s):
            if s[i:i+length] == base:
                cnt += 1
            else:
                compressed += str(cnt) + base if cnt >= 2 else base
                base = s[i:i+length]
                cnt = 1
            if i + length + 1 > len(s):
                break
            i += length
       
        compressed += str(cnt) + base if cnt >= 2 else base
        answer = min(answer, len(compressed))

    return answer