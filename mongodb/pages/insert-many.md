---
hideInToc: true
---

# Insert Many 

## 


<v-clicks> 


```python 
users = await User.insert_many(
    [
        User(name="Kamil", surname="Kulig", email="hotkamil@gmail.com"),
        User(name="John", surname="Rambo", email="nothot@gmail.com"),
        User(name="John", surname="Kowalski", email="nothot@gmail.com"),
        User(name="Mark", surname="Kowalski", email="nothot@gmail.com"),
    ]
)
[user.model_dump() for user in users]
```

Output
```python 
[
  {'id': '674ce7a11ac103c0876dd066', 'name': 'Kamil', 'surname': 'Kulig', 'email': 'hotkamil@gmail.com'}, 
  {'id': '674ce7a11ac103c0876dd067', 'name': 'John', 'surname': 'Rambo', 'email': 'nothot@gmail.com'}, 
  {'id': '674ce7a11ac103c0876dd068', 'name': 'John', 'surname': 'Kowalski', 'email': 'nothot@gmail.com'}, 
  {'id': '674ce7a11ac103c0876dd069', 'name': 'Mark', 'surname': 'Kowalski', 'email': 'nothot@gmail.com'}
]
```
</v-clicks>