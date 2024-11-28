
```python
from src.database_connection import database_init
from asyncio import run
from beanie import Document


class User(Document):
    name: str
    surname: str
    email: str


run(database_init(document_models=[User]))
```

Do you see Schema in Atlas?


Okey, but we don't have Document.

We use will use inheritance Document class same as BaseModel class.

```python
hot_adam = User(name="Adam", surname="Brzyzek", email="hotadam@gmail.com")
hot_adam
```

Output
```python
User(id=None, revision_id=None, name='Adam', surname='Brzyzek', email='hotadam@gmail.com')
```



We can see two additional attributes. `id` and `revision_id`.

`id` field reflects the unique _id field of the MongoDB document. Each object of the Document type has this field. The default type of this is PydanticObjectId.

`revision_id` field is for feature helps with concurrent operations.

We can use Base Model methods.


```python
hot_adam.model_dump()

{'id': None,
 'name': 'Adam',
 'surname': 'Brzyzek',
 'email': 'hotadam@gmail.com'}
```


Value of id field mean that we didn't insert to database yet.
