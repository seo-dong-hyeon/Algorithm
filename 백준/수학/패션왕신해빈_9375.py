import sys

T = int(sys.stdin.readline().rstrip())
for test_case in range(T):
    n = int(sys.stdin.readline().rstrip())
    dict_type_cnt = {}
    for i in range(n):
        _name, _type = sys.stdin.readline().rstrip().split()
        if _type not in dict_type_cnt:
            dict_type_cnt[_type] = 0
        dict_type_cnt[_type] += 1
    answer = 1
    for cnt in dict_type_cnt.values():
        answer *= (cnt + 1)
    answer -= 1
    print(answer)
