# pydantic + beanie = ❤️

To create Document in Collections we need to use the basic class in Beanie 
The basic class in Beanie is Document class to create collections of Document

After inspect of the Beanie base class Document, it's inherent from pydantic Base Model.

```python
import inspect
from beanie import Document
from pydantic import BaseModel

class User(Document):
    pass

assert issubclass(User, BaseModel)

inspect.getmro(Document)
```

Output
```
(beanie.odm.documents.Document,
 lazy_model.parser.new.LazyModel,
 pydantic.main.BaseModel,
 beanie.odm.interfaces.setters.SettersInterface,
 beanie.odm.interfaces.inheritance.InheritanceInterface,
 beanie.odm.interfaces.find.FindInterface,
 beanie.odm.interfaces.aggregate.AggregateInterface,
 beanie.odm.interfaces.getters.OtherGettersInterface,
 object)
```