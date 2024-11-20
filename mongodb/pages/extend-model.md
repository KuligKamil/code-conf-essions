# Extend

```python
from enum import IntEnum
from typing import Optional
from pydantic import BaseModel
from asyncio import run
from beanie import Document


class PriorityType(IntEnum):
    low = 1
    normal = 2
    urgent = 3


class SizeType(IntEnum):
    S = 1
    M = 2
    L = 3


class StatusType(IntEnum):
    BACKLOG = 1
    TODO = 2
    InProgress = 3
    OnHold = 4
    Review = 5
    Done = 6


class Task(Document):
    name: str
    description: Optional[str] = None
    priority: Optional[PriorityType] = None
    size: Optional[SizeType] = None
    status: StatusType = StatusType.BACKLOG


class User(Document):
    name: str
    surname: str
    email: str

run(database_init(document_models=[User, Task]))
```




You can always extend your Document with other classes like with pydantic classes.

For example we can add technical attribute if user is active and reuse it in the task too.


```python
from pydantic import BaseModel
from beanie import Document

class Active(BaseModel):
  active: bool = True


class User(Document, Active):
    name: str
    surname: str
    email: str

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
