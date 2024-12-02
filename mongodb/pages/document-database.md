---
layout: two-cols-header
---
# MongoDB as a Documents Database

MVP -> for User -> examples:  User or Task for User.



<v-clicks>

| SQL Database | MongoDB    |
| ------------ | ---------- |
| Table        | Collection |
| Row          | Document   |
| Column       | Field      |

</v-clicks>

::left::

<v-clicks>

SQL Table: Users

| id  | name     | email            |
| --- | -------- | ---------------- |
| 1   | John Doe | john@example.com |
| 2   | Jane Doe | jane@example.com |

</v-clicks>

::right::

<v-clicks>

MongoDB Collection: Users

```json
  [{ 
    "id": 1, "name": "John Doe", "email": "john@example.com" 
  },
  { 
    "id": 2, "name": "Jane Doe", "email": "jane@example.com" 
  }]
  ```

</v-clicks>
   
<!-- 
Imagine that we're creating an MVP for an application. <br>

Since we want to design it with users in mind, our first class will represent a User.

In MongoDB, databases hold one or more collections of documents.

Collections are analogous to tables in relational databases.

MongoDB stores data records as documents (specifically BSON documents) which are gathered together in collections.

wait BSON? JSON? not BSON

 -->

