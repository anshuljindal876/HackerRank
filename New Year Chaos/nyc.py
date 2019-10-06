arr = [1,2,5,3,7,8,6,4]

def func(q):
    count = 0
    q = [p-1 for p in q]

    for i, p in enumerate(q):
        if(p-i > 2):
            print("Too chaotic")
            return
        
        for j in range(max(p-1, 0), i):
            if(q[j] > p):
                count+=1
    print(count)
    return

func(arr)
