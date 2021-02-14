

class Sample(object):
    def __init__(self, *args, **kwargs):
        print(args)
        print(kwargs)

    def hello_world(self):
        print("hello world")
