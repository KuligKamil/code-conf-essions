---
layout: two-cols-header
hideInToc: true
---

# How use Document

<v-clicks>

Imagine that we're creating an MVP for an application. <br>
Since we want to design it with users in mind, our first class will represent a User.

Example of a User class in:

</v-clicks>
::left::

<v-clicks>

##  Pydantic

```python 
from pydantic import BaseModel


class User(BaseModel):
    name: str
    surname: str
    email: str
```
</v-clicks>

::right::

<v-clicks>

## Beanie

```python
from beanie import Document


class User(Document):
    name: str
    surname: str
    email: str
```


If you run code above, you will see error message `CollectionWasNotInitialized`.

To Initialized collection we need to connect to database.

</v-clicks>

<!-- TO Connect to database we need to install MOngodb locally or use Docker or use Mongo Atlas -->
