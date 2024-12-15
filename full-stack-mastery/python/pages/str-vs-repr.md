# str() vs repr()

Both provices string representation of an object.


| Method        | Description                              | For Whom       | Example Run                        | Example Result            |
|---------------|------------------------------------------|----------------|------------------------------------|---------------------------|
| `__repr__()`  | the official string representation for more maintainable and debuggin easier | Programmer     | `repr(today)` or `today.__repr__()` | `datetime.datetime(2023, 2, 18, 18, 40, 2, 160890)` |
| `__str__()`   | the informal string representation | User           | `str(today)` or `today.__str__()` | `2023-02-18 18:40:02.160890` |


```python
>>> import datetime
>>> today = datetime.datetime.now()

>>> repr(today)
'datetime.datetime(2023, 2, 18, 18, 40, 2, 160890)'
>>> today.__repr__()
'datetime.datetime(2023, 2, 18, 18, 40, 2, 160890)'

>>> str(today)
'2023-02-18 18:40:02.160890'
>>> today.__str__()
'2023-02-18 18:40:02.160890'
```

```python

>>> f"{today!r}"
'datetime.datetime(2023, 2, 18, 18, 40, 2, 160890)'

>>> f"{today = }"
'today = datetime.datetime(2023, 2, 18, 18, 40, 2, 160890)' 


>>> f"{today = !s}"
'today = 2023-02-18 18:40:02.160890'


$ python book.py
<__main__.Book object at 0x1025c4ed0>

# <__main__.Book object at 0x1025c4ed0>
# The name of the class and where it’s defined
# The memory address of the object:   0x1025c4ed0
```



