# Hanan Basheer (20b030018)

class bridge:
    def __init__(self, name, ports):
        self.name = name
        self.ports = ports
        self.root_bridge = name
        self.root_hop = 0
        self.root_sender = name
        self.msg = ""
        z = []
        for i in range(26):
            if chr(i+65) in ports:
                z.append("DP")
            else:
                z.append("")
        self.port_type = z
        z1 = []
        for i in range(26):
            if chr(i+65) in ports:
                z1.append(1)
            else:
                z1.append(0)
        self.trigger = z1

    def replacer(l, x, y):
        for i in range(len(l)):
            if l[i] == x:
                l[i] = y
        return l

    def rules(self, message, z):
        msg = message.split(" ")    
        if (int(str(msg[0]).lstrip("B"))<int(str(self.root_bridge).lstrip("B"))) or ((int(str(msg[0]).lstrip("B"))==int(str(self.root_bridge).lstrip("B"))) and (int(msg[1]) + 1 < int(self.root_hop))) or ((int(str(msg[0]).lstrip("B"))==int(str(self.root_bridge).lstrip("B"))) and (int(msg[1]) + 1 == int(self.root_hop)) and (int(str(msg[2]).lstrip("B"))<int(str(self.root_sender).lstrip("B")))):
            self.port_type = bridge.replacer(self.port_type, 'RP', 'DP')
            self.port_type = bridge.replacer(self.port_type, 'NP', 'DP')
            self.root_bridge = msg[0]
            self.root_hop = int(msg[1]) + 1
            self.root_sender = msg[2]
            self.port_type[ord(z)-65] = "RP"
            self.trigger[ord(z)-65] = 1
        
        elif int(str(msg[0]).lstrip("B"))==int(str(self.root_bridge).lstrip("B")) and self.port_type[ord(z)-65]=="DP" and ((int(msg[1])<int(self.root_hop)) or ((int(msg[1])==int(self.root_hop)) and int(str(msg[2]).lstrip("B"))<int(str(self.name).lstrip("B")))):
            self.port_type[ord(z)-65] = 'NP'
            self.trigger[ord(z)-65] = 0

        else:
            self.trigger[ord(z)-65] = 0

        if 'DP' not in self.port_type:
            self.port_type = bridge.replacer(self.port_type, 'RP', 'NP')
            self.trigger[ord(z)-65] = 0

    def sender(self, tr, time):
        self.msg = str(self.root_bridge) + " " + str(self.root_hop) + " " + str(self.name)
        if tr==1:
            for i in range(self.port_type.count("DP")):
                print(str(time) + " s " + self.name + " (" + self.msg.replace(" ", ",") + ")")

    def reciever(self, extendedLAN, list_bridges, tr, time):
        l = extendedLAN[self.name]
        for i in l:
            z = extendedLAN[i]
            for j in z:
                l1 = list_bridges[int(j.lstrip("B")) - 1].msg
                if l1 != "" and j != self.name and list_bridges[int(j.lstrip("B"))-1].port_type[ord(i)-65] == 'DP' and self.port_type[ord(i)-65] != 'NP':
                    self.rules(message = l1, z = i)
                    if tr==1:
                        print(str(time) + " r " + self.name + " (" + list_bridges[int(j.lstrip("B"))-1].msg.replace(" ", ",") + ")")
                elif list_bridges[int(j.lstrip("B"))-1].port_type[ord(i)-65] == 'DP':
                    self.trigger[ord(i)-65] = 0
                
def STPsimulation(list_bridges, extendedLAN, tr):
    trigger1 = -1
    time = 0
    while trigger1 != 0:
        trigger1 = 0
        for j1 in range(len(list_bridges)):
            list_bridges[j1].sender(time = time, tr = tr)
        for j1 in range(len(list_bridges)):
            list_bridges[j1].reciever(extendedLAN = extendedLAN, list_bridges = list_bridges, time = time+1, tr = tr)
        for j1 in range(len(list_bridges)):
            trigger1 += sum(list_bridges[j1].trigger)
        time += 1
    for j1 in range(len(list_bridges)):
            list_bridges[j1].sender(time = time, tr = tr)
    return list_bridges

def niceOutput(list_bridges):
    for i in range(len(list_bridges)):
        z = ""
        y = list_bridges[i].port_type
        for k in range(len(y)):
            x = y[k]
            if x!='':
                z += chr(65+k) + "-" + x + " "
        print(list_bridges[i].name + ": " + z)