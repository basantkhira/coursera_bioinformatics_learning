import math

sum = 0
with open("matrix.txt", "r") as f:
    rows = f.read().splitlines()

print(rows)
print(len(rows))
print(len(rows[0]))

  
for j in range(len(rows[0])):
    a,c,g,t = 0,0,0,0  
    for i in range(len(rows)):
        base = rows[i][j]
        match base:
            case "A":
                a += 0.1
            case "C":
                c += 0.1
            case "G":
                g += 0.1
            case "T":
                t += 0.1 
    
    entropy = 0
    if a > 0:
        entropy += -(a * math.log2(a))
    if c > 0:
        entropy += -(c * math.log2(c))
    if g > 0:
        entropy += -(g * math.log2(g))
    if t > 0:
        entropy += -(t * math.log2(t))
    sum += entropy

print (float(sum))
