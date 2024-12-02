---
layout: two-cols
hideInToc: true
---

# READ 2

## 

<v-clicks> 

Filter by name `Kamil`.

```python
best_users = await User.find(User.name == "Kamil")
best_users.to_list()
[user.model_dump() for user in best_users]
```

Output
```python 
[{
 'id': '66cb3c4631b062a669d4357c',
 'name': 'Kamil',
 'surname': 'Kulig',
 'email': 'hotkamil@gmail.com'
}]
```
</v-clicks> 

::right::

<v-clicks> 

Select what you would like to return

```python
class UserBasicInfo(BaseModel):
    name: str
    surname: str

best_users = await User.find(User.name == "Kamil")
best_users.project(UserBasicInfo).to_list()
[user.model_dump() for user in best_users]
```

Output
```python
[{
  "name": "Kamil", 
  "surname": "Kulig"
}]

```

</v-clicks>


<!-- # How to get data? 

projections

* When only a part of a document is required, projections can save a lot of database bandwidth and processing. 
  For simple projections we can just define a pydantic model with the required fields and pass it to project() method

-->