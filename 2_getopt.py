import sys, getopt


def add(a, b):
    return a+b


if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "ab", ["a", "b"])
    a = int(args[0])
    b = int(args[2])
    print(add(a, b))
