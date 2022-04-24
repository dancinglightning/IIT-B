l = input()
l = input().split(" ")

for i in range(len(l)):
    l[i] = int(l[i])

def dec(x):
    steps = 0
    for i in range(len(x)-2, -1, -1):
        z = x[i]
        x[i] = 0
        while x[i] >= x[i+1]:
            x[i] -= z
            steps += 1
    
    return steps

def inc(x):
    steps = 0
    for i in range(1, len(x)):
        z = x[i]
        x[i] = 0
        while x[i-1] >= x[i]:
            x[i] += z
            steps += 1
    
    return steps

mini = float('inf')
t = []
h = 0
k = len(l)//2
trig = 1
while h+k<len(l) and k-h>=0 and trig:
    trig = 0
    z1 = l[k-h]
    z2 = l[k+h]
    l[k-h] = 0
    if mini > dec(l[:k-h+1])+inc(l[k-h:]):
        mini = dec(l[:k-h+1])+inc(l[k-h:])
        t = l[:k-h] + l[k-h:]
        trig = 1
    l[k-h] = z1
    l[k+h] = 0
    if mini > dec(l[:k+h+1])+inc(l[k+h:]):
        mini = dec(l[:k+h+1])+inc(l[k-h:])
        t = l[:k+h] + l[:k+h]
        trig = 1
    l[k+h] = z2
    h += 1

print(mini)