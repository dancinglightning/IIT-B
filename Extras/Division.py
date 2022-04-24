x = int(input())

for i in range(x):
    z = int(input())
    if z>=1900:
        print("Division 1")
    elif z>=1600:
        print("Division 2")
    elif z>=1400:
        print("Division 3")
    else:
        print("Division 4")