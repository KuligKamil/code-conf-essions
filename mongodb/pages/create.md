---
layout: two-cols
title: CRUD
---
# CREATE

## 

<v-clicks depth="2">

To insert data to our database we could use `save` method.


⚠️ For each use, include the `await` keyword; otherwise, you will return a coroutine object and not insert the object.

```python
hot_kamil = User(name="Kamil", 
                surname="Kulig", 
                email="hotkamil@gmail.com")
```

```python
await hot_kamil.save()
```

or 

```python
await User.save(hot_kamil)
```

</v-clicks>

::right::

<v-clicks>



```python
hot_kamil.model_dump()
```

Output
```python 
{
 'id': '66cb3c4631b062a669d4357c',
 'name': 'Kamil',
 'surname': 'Kulig',
 'email': 'hotkamil@gmail.com'
}
```

You could use other methods to insert record like: `insert`, `insert_many`, `create`, `insert_one`.

</v-clicks>
