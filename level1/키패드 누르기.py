# 핸드폰 키패드 누르기
def solution(numbers, hand):
    left = [7, 4, 1]
    right = [9, 6, 3]
    result = ''
    l_position = 10
    r_position = 12

    for i in numbers: # 누르는 번호 i
        if i in left:
            result += 'L'
            l_position = i
        elif i in right:
            result += 'R'
            r_position = i
        else: # 가운데 번호라면,
            i = 11 if i == 0 else i
            l_distance = sum(divmod(abs(i - l_position), 3))
            r_distance = sum(divmod(abs(i - r_position), 3))
            if l_distance == r_distance:
                if hand == 'left':
                    result += 'L'
                    l_position = i
                else:
                    result += 'R'
                    r_position = i
            elif l_distance > r_distance:
                result += 'R'
                r_position = i
            else:
                result += 'L'
                l_position = i
    return result