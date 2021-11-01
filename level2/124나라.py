# num 수를 입력받는다.
def solution(num):
    count = 0
    # num이 1이 될 때까지 반복(num이 1이 아닐동안 반복)
    while num != 1:
        # num은 짝수인가?
        if num % 2 == 0:
            num = num / 2
            count += 1
            if count == 500:
                if num != 1:
                    return -1
                else:
                    return count
        # num은 홀수인가?
        else:
            num = num * 3 + 1
            count += 1
            if count == 500:
                if num != 1:
                    return -1
                else:
                    return count

    return count