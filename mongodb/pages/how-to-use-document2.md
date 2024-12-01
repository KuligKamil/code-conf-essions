---
layout: two-cols-header
hideInToc: true
---

# How use Document 

<v-clicks>
We will not see error message `CollectionWasNotInitialized`.

</v-clicks>
::left::

<v-clicks>


```python 
from beanie import Document


class User(Document):
    name: str
    surname: str
    email: str
```

```python 

hot_kamil = User(
    name="Kamil",
    surname="Kulig",
    email="hotkamil@gmail.com")
```

Output 


```python
{'_id': None,
 'name': 'Kamil',
 'surname': 'Kulig',
 'email': 'hotkamil@gmail.com'}
```
</v-clicks>

::right::

<v-clicks>





We need to add something to database.

</v-clicks>

