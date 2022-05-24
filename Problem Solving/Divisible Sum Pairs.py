

def divisibleSumPairs(k, ar):
    count = 0
    for i in range(len(ar)):
        for j in range(len(ar)):
            if i<j:
                if (ar[i]+ar[j]) % k == 0:
                    count+=1
    print(count)
            # if k % ar[i] + ar[j] == 0:
            # print(ar[i], ar[j])
            
arr = [1, 2, 3, 4, 5, 6]
k = 5
divisibleSumPairs(k, arr)