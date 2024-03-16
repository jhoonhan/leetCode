def solution(compare1, compare2):
    hashmap = {}
    for n in compare1:
        hashmap[n] = True
    for n in compare2:
        if n in hashmap:
            return True
    return False


compare1 = [1, 2, 3]
compare2 = [7, 4, 5]


print(solution(compare1, compare2))
