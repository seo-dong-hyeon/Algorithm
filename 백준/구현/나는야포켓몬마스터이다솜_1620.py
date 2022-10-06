import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
dict_pocket_idx = {}
dict_idx_pockect = {}

for i in range(1, N + 1):
    pocket = sys.stdin.readline().rstrip()
    dict_pocket_idx[pocket] = i
    dict_idx_pockect[i] = pocket

for _ in range(M):
    question = sys.stdin.readline().rstrip()
    if question in dict_pocket_idx:
        print(dict_pocket_idx[question])
    else:
        print(dict_idx_pockect[int(question)])
