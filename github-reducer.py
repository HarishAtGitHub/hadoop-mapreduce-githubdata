#!/usr/bin/env python2.7

from operator import itemgetter
from collections import Counter
import json
import sys

current_username = None
word = None
current_user_result = Counter({})

def printOutput(user,preference):
    for key in preference:
        print '%s,%s,%s' % (user ,key, preference[key])

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    username, statistic = line.split('\t', 1)
    languagestat = json.loads(statistic)
    # convert count (currently a string) to int
    '''try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    '''

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_username == username:
        current_user_result = current_user_result + Counter(languagestat)
    else:
        if current_username:
            # write result to STDOUT
            #print '%s\t%s' % (current_username, current_user_result)
            printOutput(current_username, current_user_result)
        current_user_result = Counter({}) + Counter(languagestat)
        current_username = username

# do not forget to output the last word if needed!
if current_username == username:
    #print '%s\t%s' % (current_username, str(current_user_result))
    printOutput(current_username, current_user_result)

