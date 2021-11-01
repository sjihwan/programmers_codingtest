def solution(s):
    s_num = s.split(" ") # 문자열로 된 숫자리스트
    num = [] # 변환된 숫자형 숫자리스트
    new = [] # 최소값, 최대값 리스트
    
    for i in s_num: # s_num의 각 원소 반복
        num.append(int(i)) # 숫자형 변환 후 num리스트에 추가
    
    new.append(str(min(num)))
    new.append(str(max(num)))

    answer = " ".join(new)
    
    return answer
