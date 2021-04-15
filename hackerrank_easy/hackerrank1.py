def simpleArraySum(n, ar):
    thesum = 0
    for i in ar:
        thesum += i
    return thesum

ar = [1,3,6,7,3,1]
test = simpleArraySum(6, ar)
print(test)