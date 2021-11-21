def solution(left, right):
    answer = 0

    # left~right 반복
    for number in range(left, right+1):
        count = 0 # 약수의 갯수 초기화
        # number의 약수를 구하기
        for num in range(1, number+1):
            if number % num == 0:
                count += 1 # 약수의 갯수 카운트
        # 약수의 갯수가 짝수인가 홀수인가
        if count % 2 == 0:
            answer += number # 갯수가 짝수인 건 더하고
        else:
            answer -= number # 갯수가 홀수인 건 뺀다
    return number

