---
layout: two-cols
hideInToc: true
---

# READ 

* **find** - basic function to get 
  * **to_list**
  * **first_or_none**
  
* get - get document with id, without filtering
* find_one - get one document with filtering
* find_all - synonyms to find({})

Get all users in database

```python
users = await User.find().to_list()
```

::right::

Get first user in database

```python
result = await User.find().first_or_none()
```

Filters Adams

```python
adams = await User.find(User.name == "Kamil").to_list()
```

Select what you would like to return

```python
class UserBasicInfo(BaseModel):
    name: str
    surname: str

TODO: check if it working!!!!!!!
adams = await User.find(User.name == "Kamil")
adams.project(UserBasicInfo).to_list()
adams
```

Output
```python
[{"name": "Kamil", "surname": "Kulig"}]

```

<!-- # How to get data? 

* When only a part of a document is required, projections can save a lot of database bandwidth and processing. 
  For simple projections we can just define a pydantic model with the required fields and pass it to project() method

-->