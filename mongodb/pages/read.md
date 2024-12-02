---
layout: two-cols-header
hideInToc: true
---

# READ 
## 

<v-clicks depth="3">

To get data from database we could use `find` method.

With two methods `to_list` and `first_or_none`.

`to_list`return list of Document Object.

For simplify change results to dict ro list of dicts.

</v-clicks>

::left:: 

<v-clicks>

Get all users in database


```python
users = await User.find().to_list()

[user.model_dump() for user in users]
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

Get one user in database

```python
user = await User.find().first_or_none()
user.model_dump()
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
</v-clicks>

<!-- # How to get data? 


* **find** - basic function to get 
  * **to_list**
  * **first_or_none**
  
* get - get document with id, without filtering
* find_one - get one document with filtering
* find_all - synonyms to find({})



-->