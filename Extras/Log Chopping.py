x = int(input())

for i in range(x):
    z = input()
    z = list(z)
    f = 0
    if "B" not in z:
        f = 1
    while "B" in z and f==0:
        x = z.index("B")
        if x==0:
            f = 1
            break
        else:
            z.pop(x-1)
            z.pop(x-1)
    
    if f:
        print("NO")
    else:
        print("YES")
    

    