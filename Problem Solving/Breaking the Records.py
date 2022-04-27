scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]



def breakingRecords(scores):
    count_min = 0
    count_max = 0
    min = 0
    max = 0
    for i in range(0, len(scores)):
        if i == 0:
            min = scores[i]
            max = scores[i]
        if min < scores[i]:
            min = scores[i]
            count_min += 1
        if max > scores[i]:
            max = scores[i]
            count_max +=1
    return [ count_min, count_max]
print(breakingRecords(scores))

