# Lets begin with argparse 
# we will compare each library method
# for implementing the following features 
# 1. commands , Arguments , Options/Flags
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


def Main():
    pass
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="this script does blah blah")
    #parser.add_argument( "-n", "--num", help=" The fibonacci number you wish to calculate.", type=int)
    #parser.add_argument( "-N", "--name", help=" provide name", type=str)
    #parser.add_argument("-o", "--output", help="output result to a file", action="store_true")
    #parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    #parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
    #args = parser.parse_args()
    #print (args.accumulate(args.integers))
