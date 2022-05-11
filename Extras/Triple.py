x1 = int(input())
for i in range(x1):
    z = int(input())
    l = input().split(" ")
    x = [l[0]]
    for j in range(1, len(l)):
        if int(l[j])<int(x[0]):
            x = [l[j]] + x
            l.pop(j)
        else:
            x = x + [l[j]]
            l.pop(j)
    
    for k in range(len(x)-1):
        print(x[k], end=" ")
    print(l[-1])
