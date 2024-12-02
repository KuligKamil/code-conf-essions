---
hideInToc: hide
layout: two-cols
---
# Example: Referencing

Use case: Task for User

<v-clicks>

```python
class User(Document):
    name: str

class Task(Document):
    name: str
    user: Link[User]

await database_init(
    document_models=[User, Task], 
    clean_database=True)

hot_kamil = User(name="Kamil")

await User.insert(hot_kamil)

tasks = [
    Task(name="cook dinner", user=hot_kamil.id),
    Task(name="do dishwasher", user=hot_kamil.id),
]
await Task.insert_many(tasks)
```
</v-clicks>

::right::

<v-clicks>

```python
users = await User.find().to_list()
[user.model_dump() for user in users]
```

Output

```python
[{
    'id': '674cebcd9f84a138a1823f1d', 
    'name': 'Kamil'
}]
```

```python
tasks = await Task.find().to_list()
[task.model_dump() for task in tasks]
```

Output

```python
[{
    'id': '674cebcd9f84a138a1823f1e', 
    'name': 'cook dinner', 
    'user': {'id': '674cebcd9f84a138a1823f1d', 
    'collection': 'User'}
}, 
{
    'id': '674cebcd9f84a138a1823f1f', 
    'name': 'do dishwasher', 
    'user': {'id': '674cebcd9f84a138a1823f1d', 
    'collection': 'User'}}]
```

</v-clicks>