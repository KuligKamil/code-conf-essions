---
title: Pydantic + ? = ❤️
---
# Pydantic + Beanie = ❤️

## 

<v-clicks>

To create Document in Collections we need to use the basic class in Beanie, Document.

Document is class to create collections of Document.

After inspect of the Beanie base class Document, it's inherent from pydantic Base Model.


```python
from beanie import Document
from pydantic import BaseModel

class User(Document):
    pass


issubclass(User, BaseModel)
```

<!-- # inspect.getmro(Document) -->
<!-- assert issubclass(User, BaseModel) -->
Output
```
True
```
</v-clicks>

<!-- 


(beanie.odm.documents.Document,
 lazy_model.parser.new.LazyModel,
 pydantic.main.BaseModel,
 beanie.odm.interfaces.setters.SettersInterface,
 beanie.odm.interfaces.inheritance.InheritanceInterface,
 beanie.odm.interfaces.find.FindInterface,
 beanie.odm.interfaces.aggregate.AggregateInterface,
 beanie.odm.interfaces.getters.OtherGettersInterface,
 object) -->