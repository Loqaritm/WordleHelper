import argparse
import re

#This is basically a simple wrapper around a simple regex. But I wanted to play around with the argparse lib

parser = argparse.ArgumentParser(description='Returns a list of words matching the input of known chars (green). Use _ to denote unknowns.')
parser.add_argument('formula', type=str, help='The formula to use. Denote unknowns known characters with themselves, unknown with _, e.g. cr_ne')
parser.add_argument('-l', '--limit', type=int, required=False, help='Limit the number of output lines')
parser.add_argument('-c', '--contains', type=str, required=False, help='All characters that without known position (yellow), e.g. pen')

args = parser.parse_args()

with open('valid-wordle-words.txt') as file:
    lines = file.readlines()
    lines = [line.strip().lower() for line in lines]

    regexFormula = args.formula.lower().replace('_', '.')

    r = re.compile(regexFormula)
    matchingList = list(filter(r.match, lines))

    if (args.limit is not None):
        matchingList = matchingList[:args.limit]

    if (args.contains is not None):
        knownChars = list(args.contains)
        matchingList = [x for x in matchingList if any(c in knownChars for c in x)]

    for match in matchingList:
        print(match)