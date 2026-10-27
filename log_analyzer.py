with open("server.log") as f:
    lines = f.readlines()

print("Log analyzer started")
print("Total lines:", len(lines))