---
layout: two-cols
hideInToc: true
---

# Relations - Referencing?

<v-clicks depth="3">

**Definition**:
  - Documents can link to other documents
  - Achieved using references

**Types of Relations**:
  - **Embedded Documents**:
    - Nested documents within a document
    - Efficient for related data accessed together
  - **Referenced Documents**:
    - Separate documents linked via ObjectId
    - Useful for large or frequently changing data


The document can contain links to other documents in their fields.

</v-clicks>

::right:: 

<v-clicks>

Example add link Task to User

```python

User = ForwardRef("User")

class User(Document):
    name: str

class Task(Document):
    name: str
    user: Link[User]

hot_adam = User(name="Adam")

await User.insert(hot_adam)

tasks = [
    Task(name="sail", user=hot_adam.id), 
    # TODO: CHECK IF IT WORKING with hot_adam without id
    Task(name="drink beers", user=hot_adam.id),
]
await Task.insert_many(tasks)
TODO: show output
TODO: create script shwo that working
```

</v-clicks>