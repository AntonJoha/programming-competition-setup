import sys
import math




def get_stdin():
    toReturn = []
    for i in sys.stdin:
        toReturn.append(i.strip())
    return toReturn


indata = get_stdin()

def make_map(indata):
    height = int(indata[0].split(" ")[0])
    to_return = []
    for i in range(height):
        to_return.append(indata[1 + i])
    return to_return, height

m, height = make_map(indata)


pos = height + 1
print(m)

def illegal(x,y, l):
    xlen = len(l)
    ylen = len(l[0])
    return x >= xlen or y >= ylen or x < 0 or y < 0

def flood_fill(x,y,l):
    if l[x][y] == 3 or illegal(x,y, l):
        return
    l[x][y] = 3
    
    perm = [
        (-1, 0),
        (1,0),
        (0,-1)
        (0,1)
    ]
    for p in perm:
        flood_fill(x + p[0], y + p[1])

def print_found(pos, l):
    points = pos.split(" ")
    sx = int(points[0]) - 1
    sy = int(points[1]) - 1
    start = l[sx][sy]
    end =  l[int(points[2]) - 1][int(points[3]) - 1]
    
    msg = ""    
    if start != end:
        print("neither")
        return
    elif start == 1:
        msg = "decimal"
    else:
        msg = "binary"

    flood_fill(int(points[0]) -1 , int(points[1]) - 1, l)
    if l[int(points[2]) - 1][int(points[3]) - 1] == 3:
        print(msg)
    else:
        print("neither")

    

for i in range(pos + 1, len(indata)):
    print_found(indata[i], m.copy())
