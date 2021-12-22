# Hash (Key, Value)
def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    # 1. participant list의 hash를 구하고, hash 값을 더한다.
    for part in participant:
        hashDict[hash(part)] = part # hashDict[Key값] = value값
        sumHash += hash(part)

    # 2. completion list의 hash를 빼준다.
    for comp in completion:
        sumHash -= hash(comp)

    # 3. 남은 값이 완주하지 못한 선수의 hash 값이 된다.
    return hashDict[sumHash]