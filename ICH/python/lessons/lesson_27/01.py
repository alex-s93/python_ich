from sys import argv
from argparse import ArgumentParser
import os

parser = ArgumentParser()
parser.add_argument('-i', '--input', help='path to input file')

args = parser.parse_args()
print(args)
