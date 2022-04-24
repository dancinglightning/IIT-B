x = int(input())

for i in range(x):
    z = int(input())
    l = input().split(" ")
    c0 = int(l[0])%2
    c1 = int(l[1])%2
    a = "YES"
    for j in range(len(l)):
        if j%2 == 0:
            if int(l[j])%2 != c0:
                a = "NO"
        if j%2 == 1:
            if int(l[j])%2 != c1:
                a = "NO"

    print(a)