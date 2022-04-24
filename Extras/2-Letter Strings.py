x = int(input())

for i in range(x):
    z = int(input())
    c = 0
    l = []
    l0 = []
    l1 = []
    for j in range(z):
        t = input()
        l.append(t)
        l0.append(t[0])
        l1.append(t[1])
    
    for a in l:
        c += l0.count(a[0]) - l.count(a)
        c += l1.count(a[1]) - l.count(a)

    print(c//2)
    print('''
    
    
    
    
    
    
    
    
    
    ''')