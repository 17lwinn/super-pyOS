# Core API guide

Importing

```python
import os_core as core
```
## service modules

```python
core.registerService("package")
```

> register a **service module**, ran on startup

> **Service modules** are system scripts that are run on startup

To make a service module, create a file like this:

---

- example.py

```python
import sys # <------ import any handy modules like sys

def init():
  # any code here
  sys.exit("hiya!")
```

- os_services.py

```python
# add them below this line

core.registerService("example")
```

------------------

## External drives
```python
core.loadDrive("F:\\")
```

> Load an external drive- **experimental**
> Read and write from the files in your drive

May accept if typed like: **F:\\\\** or **F:**