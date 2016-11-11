from collections import defaultdict
import sys
if len(sys.argv) != 6:
    print "Please enter 2 source file location and 3 output file location"
    sys.exit()

args = sys.argv

f = open(args[1], 'r')
connect = defaultdict(set)
f.readline()
line = f.readline()
while len(line) > 0:
    line = line.split(", ")
    connect[line[1]].add(line[2])
    connect[line[2]].add(line[1])
    line = f.readline()
f.close()

connect2nd = defaultdict(set)
for key in connect.keys():
    connect2nd[key] = connect[key].copy()
    for val in connect[key]:
        connect2nd[key] |= connect[val]

f = open(args[2], 'r')
f.readline()
line = f.readline()
output1 = ""
output2 = ""
output3 = ""
i = 0
while len(line) > 0:
    line = line.split(", ")
    if line[2] in connect[line[1]]:
        output1 += "trusted\n"
        output2 += "trusted\n"
        output3 += "trusted\n"
    else:
        output1 += "unverified\n"
        if line[2] in connect2nd[line[1]]:
            output2 += "trusted\n"
            output3 += "trusted\n"
        else:
            output2 += "unverified\n"
            result = "unverified\n"
            for item in connect2nd[line[1]]:
                if line[2] in connect2nd[item]:
                    result = "trusted\n"
                    break
            output3 += result

    line = f.readline()
    i += 1
    if i % 10000 == 0:
        print("Processed: %d transactions" % i)
f.close()

f = open(args[3], 'w')
f.write(output1)
f.close()
f = open(args[4], 'w')
f.write(output2)
f.close()
f = open(args[5], 'w')
f.write(output3)
f.close()
