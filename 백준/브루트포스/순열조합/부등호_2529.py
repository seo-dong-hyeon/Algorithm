import sys
from itertools import permutations

k = int(sys.stdin.readline().rstrip())
signs = sys.stdin.readline().rstrip().split()

answers = []
for nums in permutations([i for i in range(0, 10)], k + 1):
    nums = list(nums)
    flag = True
    for i, sign in enumerate(signs):
        if signs[i] == '>':
            if nums[i] < nums[i + 1]:
                flag = False
                break
        else:
            if nums[i] > nums[i + 1]:
                flag = False
                break

    if flag:
        strNum = ""
        for num in nums:
            strNum += str(num)
        answers.append(int(strNum))

answers = sorted(answers)
print(answers[-1])
print(answers[0] if len(str(answers[0])) == k + 1 else "0" + str(answers[0]))
