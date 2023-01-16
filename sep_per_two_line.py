"""
Utility Desc:
    This script seperate a text file per two line and generate a csv table, each row is the two line of the text file.
Example:
    Input:
        Hello
        你好
        Test
        测试
    Output:
        Hello,你好
        Test,测试
Usage:
    python sep_per_two_line.py input.txt -o output.csv # specify input and output file
    python sep_per_two_line.py - --reverse # read input from stdin and reverse row
"""

import argparse
import os
import sys

def parse_args():
    parser = argparse.ArgumentParser(description='Seperate a text file per two line and generate a csv table, each row is the two line of the text file.')
    parser.add_argument('input', help='Input file')
    parser.add_argument('-o', '--output', help='Output file', required=False)
    parser.add_argument('-r', '--reverse', help='Reverse row', required=False, action='store_true')
    
    args = parser.parse_args()
    if(args.input == '-'):
        args.input = sys.stdin.readlines()
    else:
        args.input = open(args.input, 'r', encoding='utf-8').readlines()
    if(args.output == None):
        args.output = 'tmp.csv'
        print('output file not specified, use default: ' + args.output)
    return args

def util_main():
    args = parse_args()
    lines = args.input
    with open(args.output, 'w', encoding='utf-8') as f:
        for i in range(0, len(lines), 2):
            if i + 1 < len(lines):
                lines[i] = lines[i].replace(',', '，')
                lines[i + 1] = lines[i + 1].replace(',', '，')
                if args.reverse:
                    f.write(lines[i + 1].strip() + ',' + lines[i].strip() + '\n')
                else:
                    f.write(lines[i].strip() + ',' + lines[i + 1].strip() + '\n')
    print('done:')
    full_path = os.path.abspath(args.output)
    print(full_path)
    
util_main()