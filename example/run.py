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

def print_found(pos, l):
    points = indata[pos].split(" ")
        
    start = 

    flood_fill(points[0] -1 , points[1] - 1, m)


for i in range(pos, len(indata)):
    print_found(indata[i], m.clone())
