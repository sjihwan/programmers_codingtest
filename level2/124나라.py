# 숫자 1, 2, 4만 사용하는 나라, 그들만의 법칙
# 숫자 n은 무엇으로 표현되는가
def solution(n):
    if n <= 3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) # divmod()함수는 (n-1)을 3으로 나눈 몫(q)과 나머지(r)를 반환
        return solution(q) + '124'[r]