# 문자열 s
# 모든 단어의 첫 문자가 대문자로, 나머지는 소문자로
def solution(s):
    answer = ''
    word = s.split(' ') # 공백을 기준으로 나눔

    for i in range(len(word)):
        # 내장함수 capitalize는 문자열을 자동으로 JadenCase로 만들어준다
        word[i] = word[i].capitalize()
        
    answer = ' '.join(word)
    
    return answer
