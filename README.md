# WordleHelper
A simple Wordle helper that looks through the list of all possible words and returns ones matching the pattern to jog your memory or to prove to yourself that yes, really, there are no words starting with UA

## Usage
```
>> python3 WordleHelper.py --help
usage: WordleHelper.py [-h] [--lower] [-l LIMIT] [-c CONTAINS] pattern

positional arguments:
  pattern               The pattern to use. Denote green characters with themselves, yellow with {char}, unknown with _, for example: C_{R}NE will return CRANE

optional arguments:
  -h, --help            show this help message and exit
  --lower               Display the output in lower characters, for those that are easily startled
  -l LIMIT, --limit LIMIT
                        Limit the number of output lines
  -c CONTAINS, --contains CONTAINS
                        All characters without known position (yellow), e.g. --contains pen
```

Example:
```
>> python3 WordleHelper.py CR_{A}E
CRAKE
CRAME
CRANE
CRAPE
CRARE
CRATE
CRAVE
CRAZE
```

## List of Wordle words taken from:
https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93
