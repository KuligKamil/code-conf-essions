
## Relations
The document can contain links to other documents in their fields.

Example add link Task to User


```python
from asyncio import run
from pydantic import BaseModel
from beanie import Document
from typing import Optional


User = ForwardRef("User")

class Task(Document, Date, Active):
    name: str
    status: StatusType = StatusType.BACKLOG
    user: Link[User]

class User(Document, Date, Active):
    name: str
    surname: str
    email: str
    address: Optional[Address] = None
    recently_tasks: Optional[list[Task]] = []


run(database_init(document_models=[User, Task], clear_database=True))

hot_adam = User(name="Adam",surname="Brzyzek",email="hotbrzyzek@gmail.com")

await User.insert(hot_adam)

tasks = [
    Task(name="sail", user=hot_adam.id), # TODO: CHECK IF IT WORKING with hot_adam without id
    Task(name="drink beers", user=hot_adam.id),
]
await Task.insert_many(tasks)
user.recently_tasks = tasks
await user.save()
```