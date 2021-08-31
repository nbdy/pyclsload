from argparse import ArgumentParser

from pyclsload import Cls, load_dir


def main():
    ap = ArgumentParser()
    ap.add_argument("-f", "--file", help="target python file path", type=str)
    ap.add_argument("-d", "--directory", help="load all files in directory", type=str)
    ap.add_argument("-c", "--cls", help="class to load")
    ap.add_argument("-m", "--method", help="method to call", type=str)
    ap.add_argument("-ca", "--class-arguments", help="arguments to pass to the class", nargs='+')
    ap.add_argument("-fa", "--function-arguments", help="Arguments to pass to the function", nargs='+')
    a = ap.parse_args()

    if a.file:
        print("Loading class '{0}' from '{1}'.".format(a.cls, a.file))
        cls = Cls(a.file, a.cls, a.class_arguments)
        print("Executing method '{0}'.".format(a.method))
        if a.function_arguments:
            cls.call(a.method, a.function_arguments)
        else:
            cls.call(a.method)
    elif a.directory:
        classes = load_dir(a.directory)
        for cls in classes:
            cls()


if __name__ == '__main__':
    main()
