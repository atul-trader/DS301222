file = open("demo.txt")
lines=[]
for line in file:
    lines.append(line.strip())
print(lines)