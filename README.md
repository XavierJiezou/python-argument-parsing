English | [简体中文](/README.zh.md)
# Introduction
There are four common ways to realize the command-line arguments parsing of Python.
- `sys.argv`
- `optparse`
- `getopt`
- `argparse`

This is a summary of all Python command-line argument parsing Modules.
# Install
They are all standard libraries of Python and do not need to be installed additionally.
# Usage
## sys.argv👍
`sys.argv` is the **simplest implementation** for parsing command-line options, which is the list of command line arguments passed to a Python script. In particular, `argv[0]` represents the script name.

---
**Recommendation**

⭐⭐⭐⭐⭐

**Example**
```python
# 1_sys.argv.py
import sys


def add(a, b):
    return a+b


if __name__ == '__main__':
    print(add(int(sys.argv[1]), int(sys.argv[2])))
```
**Running**
```bash
python 1_sys.argv.py 1 2
```
**Output**
```bash
3
```
## getopt
`getopt` module is a parser for command line options whose API is designed to be familiar to users of the C `getopt()` function, which helps scripts to parse the command line arguments in `sys.argv`. **But few people use it now, please use `argparse` module instead.**

---
**Recommendation**

⭐⭐⭐

**Example**
```python
# 2_getopt.py
import sys, getopt


def add(a, b):
    return a+b


if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "ab", ["a", "b"])
    a = int(args[0])
    b = int(args[2])
    print(add(a, b))
```
**Running**
```bash
python 2_getopt.py -a 1 -b 2
```
**Output**
```bash
3
```
## optparse
`optparse` is a more convenient, flexible, and powerful library for parsing command-line options than the old `getopt` module.

---
**Recommendation**

⭐⭐⭐⭐

**Example**
```python
# 3_optparse.py
from optparse import OptionParser


def add(a, b):
    return a+b


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-a", "--a", default=1, help="number a")
    parser.add_option("-b", "--b", default=2, help="number b")
    options, args = parser.parse_args()
    a = int(options.a)
    b = int(options.b)
    print(add(a, b))
```
**Running**
```bash
python 3_optparse.py -a 1 -b 2
```
**Output**
```bash
3
```
## argparse👍
`argparse` module makes it easy to write user-friendly command-line interfaces. Note also that `argparse` is based on `optparse`, and therefore very similar in terms of usage.

---
**Recommendation**

⭐⭐⭐⭐⭐

**Example**
```python
# 4_argparse.py
import argparse


def add(a, b):
    return a+b


if __name__=='__main__':
    # Creating a parser
    parser = argparse.ArgumentParser(description='argparse some integers.')
    # Adding arguments
    parser.add_argument('-a', '--a', default=1, type=int, required=True, help='number a')
    parser.add_argument('-b', '--b', default=2, type=int, required=True, help='number b')
    # Parsing arguments
    args = parser.parse_args()
    # Example
    a = args.a
    b = args.b
    print(add(a, b))
```
**Running**
```bash
python 4_argparse.py -a 1 -b 2
```
**Output**
```bash
3
```
# Reference
> [[1] https://docs.python.org/3/library/sys.html#sys.argv](https://docs.python.org/3/library/sys.html#sys.argv)
> 
> [[2] https://docs.python.org/3/library/getopt.html#module-getopt](https://docs.python.org/3/library/getopt.html#module-getopt)
>
> [[3] https://docs.python.org/3/library/optparse.html#module-optparse](https://docs.python.org/3/library/optparse.html#module-optparse)
>
> [[4] https://docs.python.org/3/library/argparse.html#module-argparse](https://docs.python.org/3/library/argparse.html#module-argparse)
