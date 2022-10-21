import sys

dict_vowel = {'a':True, 'e':True, 'i':True, 'o':True, 'u':True}

while True:
    try:
        word = sys.stdin.readline().rstrip()
        if word == "end":
            break
        flag = True
        vowel_flag = False
        for i, w in enumerate(word):
            # 1.모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
            if w in dict_vowel:
                vowel_flag = True
            # 2.모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
            if i >= 2:
                if w in dict_vowel and word[i - 1] in dict_vowel and word[i - 2] in dict_vowel:
                    flag = False
                    break
                if w not in dict_vowel and word[i - 1] not in dict_vowel and word[i - 2] not in dict_vowel:
                    flag = False
                    break
            # 3.같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
            if i >= 1:
                if w != 'e' and w != 'o' and w == word[i - 1]:
                    flag = False
                    break
        if not vowel_flag:
            flag = False
        if flag:
            print(f"<{word}> is acceptable.")
        else:
            print(f"<{word}> is not acceptable.")
    except:
        break