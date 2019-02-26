#!/usr/bin/python
# Arg Parse Interfaces with the python system module
# grab the arguments from the command line
# Supports checking and making sure required 
# arguments are provided
# Python fibn.py 10 
# program <fibonacci num>

# example parser = argparse.ArgumentParser()
# parser.add_argument("num", help="help text", type=int)
# args = parser.parse_args()
import argparse 

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def Main():
    pass
    

if __name__ == "__main__":
    Main()
    parser = argparse.ArgumentParser(description='fibonacci')
    parser.add_argument("num", help=" The fibonacci number you wish to calculate.", type=int)
    parser.add_argument("-o", "--output", help="output result to a file", action="store_true")

    args = parser.parse_args()
    result = fib(args.num)
    print("The "+str(args.num)+"th fib number is"+str(result))