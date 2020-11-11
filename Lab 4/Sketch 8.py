def LowestValue(array):
    for i in range(2, len(array)):
        array[i] += min( array[i - 1], array[i - 2])
    return array[-1]

arr = [1, 1000, 5000, 1]
print(LowestValue(arr))

arr = [9,5,3,5,2,4,5,3,7,8,3,7,1,9,10,1,1,10,10,7,10,3,2,6,7,2,2,10,3,8]
print(LowestValue(arr))
