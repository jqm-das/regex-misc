import math

def tjPos(t):
    x = 3108.57*math.cos(t*(math.pi/12))
    y = 3108.57*math.sin(t*(math.pi/12))
    z = 2517.8
    return x,y,z 

def satPos(t):
    x = 4534*math.cos(t*(math.pi*17/5))
    y = 0
    z = 4534*math.sin(t*(math.pi*17/5))
    return x,y,z 

def dist(t):
    a,b,c = tjPos(t)
    x,y,z = satPos(t)
    d = math.pow(a-x,2) + math.pow(b-y,2) + math.pow(c-z,2) 
    return math.pow(d,.5)

for k in range (0,1440,10):
    i = float(k/60)
    d = dist(i)
    if int(d) <= 1095:
        print(dist(i),k,i)