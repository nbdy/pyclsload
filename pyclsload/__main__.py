from argparse import ArgumentParser

from pyclsload import Cls


def main():
    ap = ArgumentParser()
    ap.add_argument("-f", "--file", help="target python file path", required=True)
    ap.add_argument("-c", "--cls", help="class to load", required=True)
    ap.add_argument("-m", "--method", help="method to call", required=True)
    ap.add_argument("-ca", "--class-arguments", help="arguments to pass to the class", nargs='+')
    ap.add_argument("-fa", "--function-arguments", help="Arguments to pass to the function", nargs='+')
    a = ap.parse_args()

    print("Loading class '{0}' from '{1}'.".format(a.cls, a.file))
    cls = Cls(a.file, a.cls, a.class_arguments)
    print("Executing method '{0}'.".format(a.method))
    if a.function_arguments:
        cls.call(a.method, a.function_arguments)
    else:
        cls.call(a.method)


if __name__ == '__main__':
    main()
