---
layout: two-cols
title: CRUD
---
# CREATE

<v-clicks depth="2">

Insert to database we need to use one of 5 options

* **insert** - basic method to insert Document
* **insert_many** - to insert one or more Documents
* **save** - insert, update current object of class Document to database
* create, insert_one - synonyms for insert 

Remember for each use await key word otherwise you will return couritne object & you will not insert object.

TODO: wrap text in slide - exmaple code

```python
hot_kamil = User(name="Kamil", 
                surname="Kulig", 
                email="hotkamil@gmail.com")
```

</v-clicks>

::right::

<v-clicks>



```python
await hot_kamil.save()
```

or 

```python
await User.save(hot_kamil)
```

or

```python
await hot_kamil.insert()
```

or

```python
await User.insert(hot_kamil)
```

```python
hot_kamil.model_dump()
```

Output
```python 
{'id': '66cb3c4631b062a669d4357c',
 'name': 'Kamil',
 'surname': 'Kulig',
 'email': 'hotkamil@gmail.com'}
```
</v-clicks>
