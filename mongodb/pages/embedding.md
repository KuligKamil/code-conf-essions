# Embbedded Document

In a relational database, you store each individual entity in its own table, and link them together through foreign keys. While MongoDB certainly supports references from one document to another, and even multi-document joins, it’s a mistake to use a document database the same way you use a relational one.


Embedded documents are an efficient and clean way to store related data, especially data that’s regularly accessed together. 

In general, when designing schemas for MongoDB, you should prefer embedding by default, and use references and application-side or database-side joins only when they’re worthwhile. The more often a given workload can retrieve a single document and have all the data it needs, the more consistently high-performance your application will be.

Link to documentation for MongoDB - Embedding MongoDB
[https://www.mongodb.com/resources/products/fundamentals/embedded-mongodb](https://www.mongodb.com/resources/products/fundamentals/embedded-mongodb)

Example Embedded Document - User Address

```python
from pydantic import BaseModel
from beanie import Document
from typing import Optional


class Address(BaseModel):
    country: str
    city: str
    street: str
    building_number: str
    zip_code: str


class User(Document):
    name: str
    surname: str
    email: str
    address: Optional[Address] = None

hot_adam = User(
    name="Adam",
    surname="Brzyzek",
    email="hotadam@gmail.com",
    address=Address(
        country="Poland",
        city="Gliwice",
        street="Jana Matejki 3",
        building_number="IBU Craft Beers",
        zip_code="44-100",
    ),
)
```


Our Favorite bar in Gliwice [https://maps.app.goo.gl/Jscx2wCmkE5cr2ke9](https://maps.app.goo.gl/Jscx2wCmkE5cr2ke9)

No they don't paying us for it. XD