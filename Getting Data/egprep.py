"""
Getting data
@date 07/01/22
@author Imran and Joel Grus
"""


"""
Reads in lines of text and spits back out the ones that match a regular expression
"""

import sys, re

regex = sys.argv[1]

for line in sys.stdin:
    if re.search(regex, line):
        sys.stdout.write(line)
