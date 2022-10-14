#!/usr/bin/env python3

__author__ = "Liang Huang"

'''python3 shannon_game.py [<text_file>]

If the argument is missing, then test.txt is used by default.
'''


from collections import Counter
#import numpy as np
import sys
import random
import math
from random import randint
from readchar import readkey

letterspace = [chr(ord('A')+i) for i in range(26)] + [' '] # 27-letter
letterset = set(letterspace)

# see https://tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html for course movement

clear = "\033[2J"
goto = lambda x,y : "\033[%d;%dH" % (x,y)
moveup = lambda x : "\033[%dA" % x
movedown = lambda x : "\033[%dB" % x
moveback = lambda x : "\033[%dD" % x
moveforward = lambda x : "\033[%dC" % x
erasetoend = "\033[K"

def take_guess(position, guess_set):    
    while True:
        print("%s_%s" % (position, moveback(1)), end="", flush=True)
        a = readkey()
        if a in ['\x03', '\x04']:
            exit(1)
        if a.upper() in guess_set: #letterspace:
            #print("you guessed:", a.upper())
            return a.upper()

def entropy(counts):
    tot = sum(counts.values())
    q = [0] + [counts[i] / tot for i in range(1,28)] + [0] # q_0 ... q_28
    # calc both lower and upper bounds
    return sum(i * math.log(i, 2) * (q[i] - q[i+1]) for i in range(1, 28)), \
           max(0, -sum(q[i] * math.log(q[i] + 1e-32, 2) for i in range(1,28)))

def play(test):
    '''
    1 Welcome
    2 ...
    3 _
    4 1
    5 2
    6 [....]    
    7 entropy:
    '''
    n = len(test)
    print(clear + goto(1, 1) + "Welcome to the Shannon Game! Please guess!")
    counts = Counter()
    for i in range(n):
        print("%s%d chars remaining%s" % (goto(2,1), n-i, erasetoend))
        avail = letterset.copy() # must copy!        
        for j in range(1, 28):
            print("%s[%s]" % (goto(6, 1),
                              "".join(x if x in avail else "-" for x in letterspace)),
                  end="", flush=True)
            key = take_guess(goto(3, i+1), avail)
            if key == test[i]:
                break
            print("%s%s%s%s" % (goto(4, i+1), "" if j<10 else j//10, goto(5,i+1), j%10), flush=True)            
            avail.discard(key)
        print("%s%s%s%s%s%d" % (goto(3, i+1), key, goto(4,i+1), "" if j<10 else j//10, goto(5, i+1), j%10), flush=True) # success
        counts [j] += 1
        low, high = entropy(counts)
        print("%sentropy in range [%.2f, %.2f]" % (goto(7, 1), low, high))        

if __name__ == "__main__":
    file = sys.argv[1] if len(sys.argv) > 1 else "test.txt"
    tests = [x.strip() for x in open(file).readlines()]
    play(tests[random.randint(0, len(tests)-1)])
