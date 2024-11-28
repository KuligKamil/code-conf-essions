---
layout: two-cols
hideInToc: true
---

# Updating 


For update we have couple options
* save
* replace -  throws: - a ValueError if the document does not have an id yet, or - a beanie.exceptions.DocumentNotFound
* update, set, inc - can be performed on the result of a find or find_one query, or on a document that was returned from an earlier query.
* upsert - to insert a document when no documents are matched against the search criteri

::right::

```python
user = await User.find(User.name == "Kamil").first_or_none()
user = await user.set({User.name: "Kean"})
user.model_dump()
```

Output
```python
{'id': '66cbc95d9721746de2ec9ee6',
 'name': 'John',
 'surname': 'Brzyzek',
 'email': 'hotbrzyzek@gmail.com'}
```


<FooterLink text="Documentation Beanie for updating and deleting" link="https://beanie-odm.dev/tutorial/updating-%26-deleting/" />