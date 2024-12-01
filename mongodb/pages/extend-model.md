---
layout: two-cols
hideInToc: true
---

# Extend Model

<v-clicks>

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

</v-clicks>


::right::


<v-clicks>

```python

class Active(BaseModel):
  active: bool = True
  
class User(Document, Active):
    name: str
    surname: str
    email: str

class Task(Document, Active):
    name: str
    
hot_kamil = User(
    name="Kamil",
    surname="Kulig",
    email="hotkamil@gmail.com")

hot_kamil.model_dump()
```

Output
```python
{'active': True,
 'id': None,
 'name': 'Kamil',
 'surname': 'Kulig',
 'email': 'hotkamil@gmail.com'}
```

</v-clicks>

<!-- 
THis is only 1 feature from Pydantic
We could spoke about validation etc
But I don't want to focus on that right now.

 -->