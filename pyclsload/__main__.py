from argparse import ArgumentParser

from pyclsload import load


def main():
    ap = ArgumentParser()
    ap.add_argument("-f", "--file", help="target python file path", required=True)
    ap.add_argument("-c", "--cls", help="class to load", required=True)
    ap.add_argument("-m", "--method", help="method to call", required=True)
    a = ap.parse_args()

    print("Loading class '{0}' from '{1}'.".format(a.cls, a.file))
    o = load(a.file, a.cls)
    print("Executing method '{0}'.".format(a.method))
    o.__dict__[a.method]()
