# 숫자와 영단어가 섞인 문자열 s
# 문자열 s를 숫자로만 바꿔서 반환
def solution(s):
    # 딕셔너리 활용!!
    str_n = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
             'eight': '8', 'nine': '9'}
    answer = s

    for key, value in str_n.items(): # items()함수는 딕셔너리의 키와 값 쌍을 모두 가져온다.
        answer = answer.replace(key, value) # key를 value로 바꿔준다.

    return int(answer)
