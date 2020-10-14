# Filesystem API guide

Importing

```python
import os_filesystem as fs
```

--------

## read and print file contents

```python
fs.readFile(file) 
fs.readFile("hi.txt") <--- example
```

Outputs:

```
hello, I know a donut
```
---------

## write to file

```python
fs.writeFile(contents, file)
fs.writeFile("hello!", "hi.txt")
```

> The function has been programmed to append the text to the end of the file, but
> might append like this:

before:
```
hello!
```

after:
```
hello!hello!
```

> Therefore any files being written to should have a new line to prevent this. We
> will try to patch it in the next updates.

---------

## delete a file

```
fs.deleteFile(file)
```

> be careful- like most things it can't be undone!