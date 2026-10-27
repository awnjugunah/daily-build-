with open("server.log") as f:
    lines = f.readlines()

print("Log analyzer started")
print("Total lines:", len(lines))

counts = {}

for line in lines:
    if "Failed" in line:
        ip = line.split()[-1]
        counts[ip] = counts.get(ip, 0) + 1

for ip, count in counts.items():
    print(ip, ":", count)