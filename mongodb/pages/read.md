# How to get data?

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

Get first user in database

```python
result = await User.find().first_or_none()
```

Filters Adams

```python
adams = await User.find(User.name == "Adam").to_list()
```