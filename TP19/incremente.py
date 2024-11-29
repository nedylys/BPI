#! usr/bin/env python3
def incremente(number,increment):
    if increment==0:
        return number
    else:
        return incremente(number,increment-1)+1
print(incremente(0,0))