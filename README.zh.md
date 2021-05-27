简体中文 | [English](/README.md)
# 引言
Python共有四种常用的实现命令行参数解析的模块，本文是对这些模块的汇总。
- `sys.argv`
- `optparse`
- `getopt`
- `argparse`
# 安装
因为它们都是Python内置的标准库，所以无需安装。
# 用法
## sys.argv👍
`sys.argv`是实现命令行参数解析最简单的方式，它是传递给Python脚本的命令行参数的列表。特别地，`argv[0]`代表脚本名。

---
**推荐**

⭐⭐⭐⭐⭐

**示例**
```python
# 1_sys.argv.py
import sys


def add(a, b):
    return a+b


if __name__ == '__main__':
    print(add(int(sys.argv[1]), int(sys.argv[2])))
```
**运行**
```bash
python 1_sys.argv.py 1 2
```
**输出**
```bash
3
```
## getopt
`getopt` 命令行参数解析模块的API设计与C引言的`getopt()`函数类似，这有助于在`sys.argv`中解析参数。**但现在几乎没人使用了， 请用`argparse`模块替代。**

---
**推荐**

⭐⭐⭐

**示例**
```python
import sys, getopt


def add(a, b):
    return a+b


if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "ab", ["a", "b"])
    a = int(args[0])
    b = int(args[2])
    print(add(a, b))
```
**运行**
```bash
python 2_getopt.py -a 1 -b 2
```
**输出**
```bash
3
```
## optparse
`optparse`是一个更方便，灵活，强大的库，用于解析命令行选项，相比于之前的`getopt`模块。

---
**推荐**

⭐⭐⭐⭐

**示例**
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
**运行**
```bash
python 3_optparse.py -a 1 -b 2
```
**输出**
```bash
3
```
## argparse👍
`argparse`让编写用户友好的命令行界面变得容易。值得注意的是，`argparse`是基于`optparse`编写的，因此两者在用法上非常相似。

---
**推荐**

⭐⭐⭐⭐⭐

**示例**
```python
import argparse


def add(a, b):
    return a+b


if __name__=='__main__':
    # 创建一个参数解析器
    parser = argparse.ArgumentParser(description='argparse some integers.')
    # 添加参数
    parser.add_argument('-a', '--a', default=1, type=int, required=True, help='number a')
    parser.add_argument('-b', '--b', default=2, type=int, required=True, help='number b')
    # 参数解析
    args = parser.parse_args()
    # 应用实例
    a = args.a
    b = args.b
    print(add(a, b))
```
**运行**
```bash
python 4_argparse.py -a 1 -b 2
```
**输出**
```bash
3
```
# 参考
> [[1] https://docs.python.org/3/library/sys.html#sys.argv](https://docs.python.org/3/library/sys.html#sys.argv)
> 
> [[2] https://docs.python.org/3/library/getopt.html#module-getopt](https://docs.python.org/3/library/getopt.html#module-getopt)
>
> [[3] https://docs.python.org/3/library/optparse.html#module-optparse](https://docs.python.org/3/library/optparse.html#module-optparse)
>
> [[4] https://docs.python.org/3/library/argparse.html#module-argparse](https://docs.python.org/3/library/argparse.html#module-argparse)
