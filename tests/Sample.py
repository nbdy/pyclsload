

class Sample(object):
    def __init__(self, *args, **kwargs):
        print(self.__class__, args)
        print(self.__class__, kwargs)

    def hello_world(self):
        print("hello world")

    def hello_args(self, *args):
        print(args)

    def hello_kwargs(self, **kwargs):
        print(kwargs)

    def hello_args_kwargs(self, *args, **kwargs):
        print(args)
        print(kwargs)
