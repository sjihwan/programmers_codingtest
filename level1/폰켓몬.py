# 총 N마리의 포켓몬 중에서 N/2마리를 가져가라.
# 최대한 다양한 종류의 포켓몬을 선택해라.
def solution(nums):
    # 폰켓몬 종류 수 variety
    variety = len(set(nums))

    # 종류 수가 가져갈 수 있는 수보다 작은 경우
    # 종류 수 반환
    if len(nums) // 2 > variety:
        return variety
    # 종류 수가 가져갈 수 있는 수보다 크거나 같은 경우
    # 가져갈 수 있는 수 반환
    else:
        return len(nums)