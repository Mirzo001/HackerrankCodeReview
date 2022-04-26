arr = [1,3,5,7,9]

def miniMaxSum(arr):
    arr.sort()
    head = sum(arr[:4:])
    tail = sum(arr[-4::])
    print(head, tail, end=' ')
miniMaxSum(arr)