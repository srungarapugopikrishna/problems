
l1 = raw_input()
l2 = raw_input()
ip1 = list(str(l1))
ip2 = list(str(l2))
ln = len(ip1) if len(ip1) > len(ip2) else len(ip2)
ip1 = ip1[::-1]
ip2 = ip2[::-1]
tot = 0
for i in range(0,ln):
    if i < len(ip1) and i < len(ip2):
        tot += int(ip1[i])*int(ip2[i])
print tot