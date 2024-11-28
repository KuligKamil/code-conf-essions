---
layout: two-cols
hideInToc: true
---

# Extend

You can always extend your Document with other classes like with pydantic classes.

For example we can add technical attribute if user is active and reuse it.

```python
class User(Document):
    name: str
    surname: str
    email: str
    active: bool = True

class Task(Document):
    name: str
    active: bool = True
```

<!-- We would like to extend User for technical attribute. -->

::right::



```python

class Active(BaseModel):
  active: bool = True
  
class User(Document, Active):
    name: str
    surname: str
    email: str

class Task(Document, Active):
    name: str
    
hot_adam = User(
    name="Adam",
    surname="Brzyzek",
    email="hotadam@gmail.com")

hot_adam.model_dump()
```

Output
```python
{'active': True,
 'id': None,
 'name': 'Adam',
 'surname': 'Brzyzek',
 'email': 'hotadam@gmail.com'}
```
