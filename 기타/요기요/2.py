import spacy

nlp = spacy.load("en_core_web_sm")

def anonymize_text(sentences):
    answer = ""

    doc = nlp(sentences)
    past = ""
    for i, e in enumerate(doc):
        plus = ""
        # 사람이름이면 X으로 대체
        if e.ent_type_ == "PERSON":
            for _ in range(len(e)):
                plus += "X"
        else:
            plus += str(e)
            
        # 현재 단어가 사람이름인지 저장
        now = True if e.ent_type_ == "PERSON" else False
        # 두 번째 단어부터
        if i != 0:
            # 점이면 그냥 저장
            if plus == '.':
                answer += plus       
            else:
                # 이전과 현재 모두 사람이름이면 붙여서 저장
                if past and now:
                    answer = answer + 'X' + plus
                # 아니라면 띄어쓰기
                else:
                    answer = answer + ' ' + plus    
        else:
            answer = plus
        # 이전 단어가 사람이름인지 저장
        past = True if e.ent_type_ == "PERSON" else False
    
    return answer