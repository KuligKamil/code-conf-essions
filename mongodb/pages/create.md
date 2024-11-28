---
layout: two-cols
title: CRUD
---
# CREATE

Insert to database we need to use one of 5 options

* **insert** - basic method to insert Document
* **insert_many** - to insert one or more Documents
* **save** - insert, update current object of class Document to database
* create, insert_one - synonyms for insert 

Remember for each use await key word otherwise you will return couritne object & you will not insert object.

::right::


```python
hot_adam = User(name="Adam", surname="Brzyzek", email="hotadam@gmail.com")
```

```python
await hot_adam.save()
```
 or 

```python
await User.save(hot_adam)
```
 or

```python
await hot_adam.insert()
```

 or

```python
await User.insert(hot_adam)
```

```python
hot_adam.model_dump()
```

Output
```python 
{'id': '66cb3c4631b062a669d4357c',
 'name': 'Adam',
 'surname': 'Brzyzek',
 'email': 'nothotadam@gmail.com'}
```