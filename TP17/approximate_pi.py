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
    for _ in range(n):
        x=uniform(-1,1)
        y=uniform(-1,1)
        if sqrt(x**2+y**2)<=1:
            cpt+=1
            points.append([x,y,True])
        else:
            points.append([x,y,False])
    print(cpt/n*4)
    return cpt/n*4,points
if __name__=="__main__":
    main()
