arr = [
    [1,1,1,0,0,0],
    [0,1,0,0,0,0],
    [1,1,1,0,0,0],
    [0,0,2,4,4,0],
    [0,0,0,2,0,0],
    [0,0,1,2,4,0]]

hourSum = -100
for i in range(4):
    for j in range(4):
        s = arr[i+1][j+1]
        for k in range(j, j+3):
            s+=arr[i][k]
        for k in range(j, j+3):
            s+=arr[i+2][k]
        hourSum = max(hourSum, s)

print(hourSum)
