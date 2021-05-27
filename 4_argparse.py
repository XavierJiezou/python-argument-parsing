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
