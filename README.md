# pyclsload
easily load classes from source files<br>
basically just a wrapper for importlib
## why?
```python
# doesn't look
from pyclsload import load
o = load("somefile.py", "ThisAClass")
o.somemethod()

# better than
from importlib.util import spec_from_file_location, module_from_spec
s = spec_from_file_location("ThisAClass", "somefile.py")
o = module_from_spec(s)
s.loader.exec_module()
o.somemethod()
```

## install
```shell
pip3 install pyclsload
```