from importlib.util import spec_from_file_location, module_from_spec


def load(file_path: str, class_name: str):
    s = spec_from_file_location(class_name, file_path)
    m = module_from_spec(s)
    s.loader.exec_module()
    return m


__all__ = ['load']
