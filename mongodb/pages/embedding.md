---
layout: two-cols
title:  Embedding vs. Referencing
---
# Embbedded Document


<v-clicks depth="3">


- **Definition**:
  - Documents within documents
  - Nested structure

- **Advantages**:
  - Efficient data retrieval
  - Reduces need for joins
  - Keeps related data together

- **Use Cases**: Storing related data accessed together

</v-clicks>

::right::

<v-clicks>

Example: User profile with address

```python
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

Link to documentation for MongoDB - Embedding MongoDB
[https://www.mongodb.com/resources/products/fundamentals/embedded-mongodb](https://www.mongodb.com/resources/products/fundamentals/embedded-mongodb)

</v-clicks>

<!--


In a relational database, you store each individual entity in its own table, and link them together through foreign keys. While MongoDB certainly supports references from one document to another, and even multi-document joins, it’s a mistake to use a document database the same way you use a relational one.


Embedded documents are an efficient and clean way to store related data, especially data that’s regularly accessed together. 

 In general, when designing schemas for MongoDB, you should prefer embedding by default, and use references and application-side or database-side joins only when they’re worthwhile. The more often a given workload can retrieve a single document and have all the data it needs, the more consistently high-performance your application will be.





## Relational vs Document Databases

- **Relational DB**: 
  - Entities in separate tables
  - Linked via foreign keys
  - Supports references and joins

- **MongoDB**:
  - Prefer embedding documents
  - Efficient for related data accessed together
  - Use references and joins sparingly

### Schema Design Tips
- Embed by default
- Use references/joins only when necessary
- Aim for single document retrieval for high performance

 -->

