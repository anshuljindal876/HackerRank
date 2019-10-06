a = [1,2,3,4,5]
d = int(input())

a = a[d:len(a)] + a[:d]
print(a)
