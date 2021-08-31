from importlib.util import spec_from_file_location, module_from_spec


def load(file_path: str, class_name: str, *args, **kwargs):
    s = spec_from_file_location(class_name, file_path)
    m = module_from_spec(s)
    s.loader.exec_module(m)
    return m.__dict__[class_name](*args, **kwargs)


class Cls(object):
    cls = None

    def __init__(self, file_path: str, class_name: str, *args, **kwargs):
        self.cls = load(file_path, class_name, *args, **kwargs)
        self.file_path = file_path
        self.class_name = class_name
        self.args = args
        self.kwargs = kwargs

    def call(self, name: str, *args, **kwargs):
        if hasattr(self.cls, name):
            return getattr(self.cls, name)(*args, **kwargs)
        return None


__all__ = ['load', 'Cls']
