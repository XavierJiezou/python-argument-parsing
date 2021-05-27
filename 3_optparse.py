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
