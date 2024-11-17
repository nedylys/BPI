#! usr/bin/env python3
import sys
from random import uniform
from math import sqrt
def main():
    if __name__=="__main__":
       n=int(sys.argv[1])
    else:
        n=int(sys.argv[2])
    cpt=0
    points=[]
    bon_points=[]
    for _ in range(n):
        x=uniform(-1,1)
        y=uniform(-1,1)
        if sqrt(x**2+y**2)<=1:
            cpt+=1
            bon_points.append((x,y))
        else:
            points.append((x,y))
    print(cpt/n*4)
    return cpt/n*4,points,bon_points
if __name__=="__main__":
    main()
