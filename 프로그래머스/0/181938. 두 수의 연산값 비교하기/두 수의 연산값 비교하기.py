def solution(a, b):
    concatAB=int(str(a)+str(b))
    answer = concatAB if concatAB > 2*a*b else 2*a*b
    return answer