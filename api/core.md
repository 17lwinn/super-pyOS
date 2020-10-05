# Core API guide

```python
core.registerService("package")
```

> register a **service module**, ran on startup

> **Service modules** are system scripts that are run on startup

To make a service module, create a file like this:

> example.py
```python
import sys # <------ import any handy modules like sys

def init():
  # any code here
  sys.exit("hiya!")
```

> main.py
```python

```