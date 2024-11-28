---
layout: two-cols-header
---
# JSON vs. BSON


JSON (JavaScript Object Notation) and BSON (Binary JSON) are both data interchange formats with key differences.


| Feature                       | JSON                                                   | BSON                                         |
| ----------------------------- | ------------------------------------------------------ | -------------------------------------------- |
| Format                        | Text-based, human-readable                             | Binary format, not human-readable            |
| Common Usage                  | APIs, configuration files, data interchange on the web | MongoDB for efficient storage and retrieval  |
| Traversal Speed               | Slower due to variable-length elements                 | Faster with fixed-length elements            |
 Data Types and Metadata       | Limited (no datetime or binary data, lacks metadata)   | Supports additional types (datetime, binary), includes metadata and type information |


 

<FooterLink text="Official docs MongoDB, JSON and BSON" link="https://www.mongodb.com/resources/basics/json-and-bson" />