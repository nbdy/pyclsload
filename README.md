# pyclsload
[![CodeFactor](https://www.codefactor.io/repository/github/nbdy/pyclsload/badge)](https://www.codefactor.io/repository/github/nbdy/pyclsload)
easily load classes from source files<br>
basically just a wrapper for importlib
## why?
```python
# doesn't look
from pyclsload import load_cls
o = load_cls("somefile.py", "ThisAClass")
o.somemethod()

# better than
from importlib.util import spec_from_file_location, module_from_spec
s = spec_from_file_location("ThisAClass", "somefile.py")
o = module_from_spec(s)
s.loader.exec_module()
o.somemethod()
```
## features
- [X] load_cls
- [X] init_cls
- [X] load_dir (based on the premise that the class is called like the module)
## install
```shell
pip3 install pyclsload
```