# 문자열 s, 공백으로 구성된 숫자들
# "최소값 최대값" 반환
def solution(s):
    s_num = s.split(" ") # # 문자열을 공백을 기준으로 나눈 숫자리스트
    num = [] # 변환될 숫자형 숫자리스트
    new = [] # 최소값, 최대값 리스트
    
    for i in s_num: # s_num의 각 원소 반복
        num.append(int(i)) # 숫자형 변환 후 num리스트에 추가
    
    # 최소값, 최대값을 문자형으로 변환
    new.append(str(min(num)))
    new.append(str(max(num)))

    answer = " ".join(new) # "최소값 최대값" 형태로 반환하기 위해
    
    return answer
