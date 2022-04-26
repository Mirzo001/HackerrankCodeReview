

# candles = [4,4,1,3]

# def birthdayCakeCandles(candles):
#     number_occur = {}
#     for i in range(len(candles)):
#         if candles[i] in number_occur:
#             number_occur[candles[i]]+=1
#         else:
#             number_occur[candles[i]] = 1
#     keysa = list(number_occur.keys())
#     keysa.sort()
#     return number_occur[keysa[-1]]
# print(birthdayCakeCandles(candles))




candles = [4,4,4,1,1,3,3,3,3,5]

def birthdayCakeCandles(candles):
    candles.sort()
    count = 0
    for i in range(len(candles)-1, 1, -1):
        if candles[i] == candles[i-1]:
            count+=1
        else:
            count+=1
            break
    print(count)
birthdayCakeCandles(candles)