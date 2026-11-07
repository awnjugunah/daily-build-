with open("auth.log") as f:
    lines = f.readlines()

counts= {}

for line in lines :
    if "Failed" in line:
        parts =line.split()
        ip =parts[7]
        counts[ip]=counts.get(ip ,0) +1

for ip, count in counts.items():
    print(ip,":",count)
