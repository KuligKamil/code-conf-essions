---
hideInToc: true
---

# How use Document 

<v-clicks>

We will not see error message `CollectionWasNotInitialized`.

```python 
from beanie import Document

class User(Document):
    name: str
    surname: str
    email: str
```

```python 
hot_kamil = User(name="Kamil", surname="Kulig", email="hotkamil@gmail.com")
hot_kamil.model_dump()
```

Output 


```python
{
 '_id': None,
 'name': 'Kamil',
 'surname': 'Kulig',
 'email': 'hotkamil@gmail.com'
 }
```

The _id is None because the document has not been added to the database yet.

</v-clicks>


<!-- In next slides if I show something in Output as a dict should be Document Object.
 -->
