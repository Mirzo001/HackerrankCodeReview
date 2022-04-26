s = 7 
t = 11
a = 5
b = 15
m = 3
n = 2
apples = [-2, 2, 1]
oranges = [5, -6]
def countApplesAndOranges(s, t, a, b, apples, oranges):
    countapple = 0
    countorange = 0
    for i in range(0, len(apples)):
        apples[i]+= a
    for i in range(0, len(oranges)):
        oranges[i]+= b
    for i in range(0, len(apples)):
        if apples[i] >= s and apples[i] <= t:
            countapple+=1
    for i in range(0, len(oranges)):
        if oranges[i] >= s and oranges[i] <= t:
            countorange+=1
    print(countapple)
    print(countorange)
countApplesAndOranges(s, t, a, b, apples, oranges)