from argparse import ArgumentParser

from pyclsload import load


def main():
    ap = ArgumentParser()
    ap.add_argument("-f", "--file", help="target python file path", required=True)
    ap.add_argument("-c", "--cls", help="class to load", required=True)
    ap.add_argument("-m", "--method", help="method to call", required=True)
    a = ap.parse_args()

    print("Loading class '{0}' from '{1}'.".format(a.cls, a.file))
    o = load(a.file, a.cls, ("yeee", ), kwargs={"yorg"})
    print("Executing method '{0}'.".format(a.method))
    o.hello_world()


if __name__ == '__main__':
    main()
