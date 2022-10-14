# Shannon Game for Human Language Model Entropy

This project implements a simple [Shannon game](https://classes.engr.oregonstate.edu/eecs/fall2022/ai539-003/extra/Shannon1950.pdf) to estimate the entropy of human language models,
for my [NLP class](https://classes.engr.oregonstate.edu/eecs/fall2022/ai539-003) (Fall 2022, Oregon State).

It was inspired by the Java Applet from UCSD's [Math 187 class](https://mathweb.ucsd.edu/~crypto/) (Cryptography, Spring 2014) by 
[Prof. Adriano Garsia](https://mathweb.ucsd.edu/~garsia/). Since Java Applets have become obsolete, I wrote this very simple Python tool as a replacement for my students. It uses [ANSI escape sequences for cursor movement](https://tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html).

## Installation

This package uses the `readchar` library.

```
pip3 install -r requirements.txt
```

## Usage

On a Linux/Mac terminal (better with wide screen), run

```
python3 shannon_game.py [<text_file>]
```

If the argument is missing, `test.txt` is used by default.

A typical screenshot is:

```
Welcome to the Shannon Game! Please guess!
118 chars remaining
EVEN THOUGH YOU _
2           2
01121413411161117
[-BCD-FGHIJKL-NOPQ--TUV-XYZ-]
entropy in range [1.44, 1.80]
```

## Entropy Estimation

This project uses Shannon's original estimates of the lowerbound and the upperbound, but using `N=1` (i.e., unigram guess sequence).

## Author
Liang Huang (liang.huang.sh@gmail.com)