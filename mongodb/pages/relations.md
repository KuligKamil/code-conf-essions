---
hideInToc: true
---

# Types of Relations

<v-clicks>

| Feature     | Embedded Documents                                            | Referenced Documents                                           |
| ----------- | ------------------------------------------------------------- | -------------------------------------------------------------- |
| Structure   | Nested documents within a document                            | Documents can link to other documents                          |
| Efficiency  | Efficient for related data accessed together                  | Useful for large or frequently changing data                   |
| Data Access | Accessed together with the parent document                    | Separate documents linked via ObjectId                         |
| Use Case    | Best for small, tightly coupled data                          | Best for large, loosely coupled data                           |

</v-clicks>
