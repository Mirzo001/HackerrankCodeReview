a = [17, 28, 30]
b = [99, 16, 8]

def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(0, 3):
        a[i] = int(a[i])
        b[i] = int(b[i])
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
        else:
            pass
    return [alice, bob]
        
        
result = (compareTriplets(a, b))
print(result)