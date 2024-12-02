---
layout: two-cols
title:  Embedding vs. Referencing
---
# Example: Embbedding


<v-clicks depth="3">

Use Case: User profile with address

```python
class Address(BaseModel):
    country: str
    city: str
    street: str
    building_number: str

class User(Document):
    name: str
    surname: str
    email: str
    address: Optional[Address] = None

await database_init(document_models=[User], clean_database=True)

hot_kamil = User(
    name="Kamil",
    surname="Kulig",
    email="hotkamil@gmail.com",
    address=Address(
        country="Wakanda",
        city="Gotham",
        street="Elm Street",
        building_number="2137",
    ),
)
```
</v-clicks>

::right::

<v-clicks>

```python 
await hot_kamil.insert()

user = await User.find().first_or_none()

user.model_dump()
```

Output: 

```python
{
  'id': '674cee131b2757808753133e', 
  'name': 'Kamil', 
  'surname': 'Kulig', 
  'email': 'hotkamil@gmail.com', 
  'address': {
    'country': 'Wakanda', 
    'city': 'Gotham', 
    'street': 'Elm Street', 
    'building_number': '2137'
  }
}

```
<FooterLink text="Documentation MongoDB - Embedding MongoDB" link="https://www.mongodb.com/resources/products/fundamentals/embedded-mongodb"/>

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

