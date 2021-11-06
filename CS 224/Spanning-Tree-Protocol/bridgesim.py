# Hanan Basheer (20b030018)

from bridge import *

list_bridges = []
final = {}
extendedLAN = {}
trace = int(input())
n = int(input())
for i in range(n):
    x = input()
    y = x[0:2]
    ports1 = x[4:].split(" ")
    b = bridge(name = y, ports = ports1)
    extendedLAN[y] = ports1
    for j in range(len(ports1)):
        if ports1[j] in final:
            final[ports1[j]] = final[ports1[j]] + [y]
        else:
            final[ports1[j]] = [y]
    list_bridges.append(b)

extendedLAN.update(final)
list_bridges = STPsimulation(list_bridges, extendedLAN, tr = trace)
niceOutput(list_bridges)