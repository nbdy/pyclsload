from importlib.util import spec_from_file_location, module_from_spec
from os import listdir
from os.path import join


def load_cls(file_path: str, class_name: str):
    s = spec_from_file_location(class_name, file_path)
    m = module_from_spec(s)
    s.loader.exec_module(m)
    return m.__dict__[class_name]


def load_dir(directory: str) -> list:
    r = []
    for fn in listdir(directory):
        r.append(load_cls(join(directory, fn), fn.split(".")[0]))
    return r


def init_cls(file_path: str, class_name: str, *args, **kwargs):
    m = load_cls(file_path, class_name)
    return m.__dict__[class_name](*args, **kwargs)


class Cls(object):
    cls = None

    def __init__(self, file_path: str, class_name: str, *args, **kwargs):
        self.cls = init_cls(file_path, class_name, *args, **kwargs)
        self.file_path = file_path
        self.class_name = class_name
        self.args = args
        self.kwargs = kwargs

    def call(self, name: str, *args, **kwargs):
        if hasattr(self.cls, name):
            return getattr(self.cls, name)(*args, **kwargs)
        return None


__all__ = ['load_cls', 'init_cls', 'Cls']
