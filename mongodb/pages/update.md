---
layout: two-cols
hideInToc: true
---

# Updating 

<v-clicks>

For update we have couple options
* save
* replace - throws exceptions: ValueError or DocumentNotFound
* update, set, inc - can be performed on the result of a find query, or on a document that was returned from an earlier query
* upsert - to insert a document when no documents are matched against the search criteria

</v-clicks>

::right::

<v-clicks>

```python
user = User.find(User.name == "Kamil")
user = await first_or_none()
user = await user.set({User.name: "Keanu"})
user.model_dump()
```

Output
```python
{
  'id': '66cbc95d9721746de2ec9ee6',
 'name': 'Keanu',
 'surname': 'Kulig',
 'email': 'hotkulig@gmail.com'
}
```


<FooterLink text="Documentation Beanie for updating and deleting" link="https://beanie-odm.dev/tutorial/updating-%26-deleting/" />

</v-clicks>

<!--  
 ValueError if the document does not have an id yet 
 DocumentNotFound if the document does not exists
 -->