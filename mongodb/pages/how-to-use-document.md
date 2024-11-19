# How use Document

Imagine that we're creating an MVP for an application. Since we want to design it with users in mind, our first class will represent a User.

Here's an example of a User class in Pydantic:"

```python 
from pydantic import BaseModel


class User(BaseModel):
    name: str
    surname: str
    email: str
```

Example in User class in beanie

```python
from beanie import Document


class User(Document):
    name: str
    surname: str
    email: str
```


if you run code above, you will see error message `CollectionWasNotInitialized`.
To Initialized collection need to use init_beanie function.