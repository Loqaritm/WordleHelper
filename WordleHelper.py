import argparse
import re

# This is basically a simple wrapper around a simple regex. But I wanted to play around with the argparse lib

parser = argparse.ArgumentParser(description='A simple Wordle helper that looks through the list of all possible words and returns ones matching \
the pattern to jog your memory or to prove to yourself that yes, really, there are no words starting with UA___')
parser.add_argument('pattern', type=str, help='The pattern to use. Denote green characters with themselves, yellow with {char}, unknown with _,\n\
for example: C_{R}NE will return CRANE')
parser.add_argument('-l', '--limit', type=int, required=False, help='Limit the number of output lines')
parser.add_argument('-c', '--contains', type=str, required=False, help='All characters that without known position (yellow), e.g. --contains pen')

args = parser.parse_args()

with open('valid-wordle-words.txt') as file:
    lines = file.readlines()
    lines = [line.strip().lower() for line in lines]

    inputPattern = args.pattern.lower()

    # Find all the yellow characters
    yellowCharactersInPattern = re.findall(r'.*\{(.)\}.*', inputPattern)

    # Replace yellow characters in pattern with _ (meaning any characters)
    inputPattern = re.sub(r'\{.\}', '_', inputPattern)
    
    regexPattern = inputPattern.replace('_', '.')
    r = re.compile(regexPattern)
    matchingList = list(filter(r.match, lines))

    if (args.limit is not None):
        matchingList = matchingList[:args.limit]

    if (args.contains is not None or yellowCharactersInPattern):
        knownChars = list(args.contains) + yellowCharactersInPattern
        matchingList = [x for x in matchingList if all(c in x for c in knownChars)]

    for match in matchingList:
        print(match)