---
hideInToc: true
layout: two-cols
---

# Simple queries in MongoDB Atlas 
Cheat sheet [MongoDB Atlas filter](https://www.mongodb.com/docs/compass/current/query/filter/).

<!-- TODO: add example in Beanie  -->


Logical:
1. **AND**: `{ $and: [ { field: value, field: value } ] }`
2. **OR**: `{ $or: [ { field: value }, { field: value } ] }`
3. **NOT**: `{ field: { $not: { $eq: value } } }`
4. **NOR**: `{ $nor: [ { field: value }, { field: value } ] }`

::right::

Comparison:
1. **Greater than**: `{ field: { $gt: value } }`
2. **Greater than or equal**: `{ field: { $gte: value } }`
3. **Less than**: `{ field: { $lt: value } }`
4. **Less than or equal**: `{ field: { $lte: value } }`
5. **In an array**: `{ field: { $in: [value1, value2, ... valueN ] } }`
6. **Not in an array**: `{ field: { $nin: [ value1, value2 ... valueN ] } }`
7. **Equal to**: `{ field: { $eq: value } }`
8. **Not equal to**: `{ field: { $ne: value } }`
 

Embedded Field: `{ "field.embedded_field": value }`
Exists: `{ field: { $exists: boolean } }`
Type: `{ field: { $type: BSON type } }`
Any of the listed types: `{ field: { $type: [ BSON type1 , BSON type2, ... BSON typeN ] } }`

<!-- 
In MongoDB Atlas you can browse data from your database. On the page, you need to select Clusters from the options on the left bar and then press button **`Browse Collection`**. From this level of the page you can see the **filter field** used for query data. You can use all the MongoDB [query operators](https://www.mongodb.com/docs/manual/reference/operator/query/) except the *\$text* and *\$expr* operators.
*Let's create some queries in MongoDB Altas.*

**Exercise 10** - Search for user with id. 

*`HINT`: BSON object to contain id in mongo db is `ObjectId()`.*

<b><i>Solution to Exercise 10.</i></b>

```javascript
{_id: ObjectId("66cb3940ad0f1a3e611edd3b")}
```



**Exercise 11** - Search for user which surname is `Olko`.

<b><i>Solution to Exercise 11.</i></b>

```javascript
{surname: "Olko"}
```



**Exercise 12** - Search for users whose city address is `Warszawa`.

<b><i>Solution to Exercise 12.</i></b>

```javascript
{"address.city": "Warszawa"}
```



**Exercise 13** - Search for users whose name is `Krzysztof`, `Nicole` or `Angelika`.

<b><i>Solution to Exercise 13.</i></b>

```javascript
{"name": {$in: ["Krzysztof", "Nicole", "Angelika"]}}
```
```javascript
{$or: [{"name": "Krzysztof"}, {"name": "Nicole"}, {"name": "Angelika"}]}
```



**Exercise 14** - Search for tasks whose priority is `low` or status is `Review`. 

*`HINT`: Priority int enum for `low is 1` and status int enum for `Review is 5`.*

<b><i>Solution to Exercise 14.</i></b>

```javascript
{$or: [{priority: 1}, {status: 5}]}
```



**Exercise 15*** - Search for all active tasks whose creation date is after `2024-07-18`.

*`HINT`: BSON object for date in mongo db is `ISODate()`.*

<b><i>Solution to Exercise 15.</i></b>

```javascript
{active: true, create_date: {$gt: ISODate("2024-07-18")}}
```



### Exercise X - create crud for User, Task & TaskLogStatus

create functions, for example
* get task for specific user id
* get all tasks from active users
* get created logs in date range
* create User, Task & TaskLogStatus
* delete/deactivate user, task & TaskLogStatus

<b><i>Solution</i></b>
Come on. Again?! XD
 -->
