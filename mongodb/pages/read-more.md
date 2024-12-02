---
# layout: two-cols-header
hideInToc: true
---

# Read More - Operators

##

<v-clicks> 

There is a lot of operators implement in Beanie.

Logic: And, Or, Nor, Not, Comparison: Eq, GT, GTE...



Example with OR

```python
from beanie.operators import Or

users = User.find(Or(
  User.name == "John", 
  User.surname == "Kulig"
))
users = await users.to_list() 
[user.model_dump() for user in users]
```

Output
```python
[
  {'id': '674ce6ed73bd3b6e608e34de', 'name': 'Kamil', 'surname': 'Kulig', 'email': 'hotkamil@gmail.com'}, 
  {'id': '674ce6ed73bd3b6e608e34df', 'name': 'John', 'surname': 'Rambo', 'email': 'nothot@gmail.com'}, 
  {'id': '674ce6ed73bd3b6e608e34e0', 'name': 'John', 'surname': 'Kowalski', 'email': 'nothot@gmail.com'}
]

```

<FooterLink text="More about operators in Beanie" link="https://beanie-odm.dev/api-documentation/operators/find/"/>

</v-clicks>

<!-- what will be if I change OR to AND
it will be empty list

-->