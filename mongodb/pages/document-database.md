---
layout: two-cols-header
---
# Mongodb as a Documents Database

<!-- ## Comparison between SQL and MongoDB -->

| SQL Database | MongoDB    |
| ------------ | ---------- |
| Table        | Collection |
| Row          | Document   |
| Column       | Field      |

<!-- ## Example: -->

::left::

SQL Table: Users

| id  | name     | email            |
| --- | -------- | ---------------- |
| 1   | John Doe | john@example.com |
| 2   | Jane Doe | jane@example.com |


::right::

MongoDB Collection: Users

```json
  [{ 
    "_id": 1, "name": "John Doe", "email": "john@example.com" 
  },
  { 
    "_id": 2, "name": "Jane Doe", "email": "jane@example.com" 
  }]
  ```

   
<!-- 


In MongoDB, databases hold one or more collections of documents.

Collections are analogous to tables in relational databases.

MongoDB stores data records as documents (specifically BSON documents) which are gathered together in collections.

wait BSON? JSON? not BSON

 -->

