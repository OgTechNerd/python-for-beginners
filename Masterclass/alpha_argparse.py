#!/usr/bin/python3

import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="this script does blah blah")
    subparsers = parser.add_subparsers(help='sub-command help')
    parser_a = subparsers.add_parser('a', help='a help')
    parser_a.add_argument('bar', type=int, help='bar help')
    parser_b = subparsers.add_parser('b', help='b help')
    parser_b.add_argument('--baz', choices='XYZ', help='baz help')
    parser.add_argument( "-n", "--num", help=" The fibonacci number you wish to calculate.", type=int)
    parser.add_argument( "-N", "--name", help=" provide name", type=str)
    parser.add_argument("-o", "--output", help="output result to a file", action="store_true")
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
    args = parser.parse_args()
    
