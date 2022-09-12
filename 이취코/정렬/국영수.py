import sys

N = int(sys.stdin.readline().rstrip())
dic_student = {}

for _ in range(N):
    name, kor, eng, mat = sys.stdin.readline().rstrip().split()
    dic_student[name] = [int(kor), int(eng), int(mat), name]

for key, value in sorted(dic_student.items(), key = lambda x: (-x[1][0], x[1][1], -x[1][2], x[1][3])):
    print(key)