from itertools import combinations # 내장 라이브러리itertools 조합함수combinations

def check(a, b, c):
    total = a + b + c
    for n in range(2, total):
        if total % n == 0:
            return False
    return True

def solution(nums):
    answer = 0
    C = list(combinations(nums, 3))
    for i in A:
        if check(i[0], i[1], i[2]):
            answer += 1
    return answer