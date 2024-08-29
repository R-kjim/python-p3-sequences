#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    if length==0:
        output=[]
    elif length<=2:
        output=[0] if length==1 else [0,1]
    elif length>2:
        output=[0,1]+[None]*(length-2)
        len1=2
        while len1<length:
            output[len1]=sum(output[0:len1][-2:])
            len1+=1
    print(output)

print_fibonacci(6)
