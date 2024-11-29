---
layout: two-cols-header
---
# JSON vs. BSON

<v-clicks>

 Both are data interchange formats with key differences.

</v-clicks>

<v-clicks>


| Feature                       | JSON - JavaScript Object Notation                                                  | BSON - Binary JSON                                        |
| ----------------------------- | ------------------------------------------------------ | -------------------------------------------- |
| Format                        | Text-based, human-readable                             | Binary format, not human-readable            |
| Common Usage                  | APIs, configuration files, data interchange on the web | MongoDB for efficient storage and retrieval  |
| Traversal Speed               | Slower due to variable-length elements                 | Faster with fixed-length elements            |
 Data Types and Metadata       | Limited (no datetime or binary data, lacks metadata)   | Supports additional types (datetime, binary), includes metadata and type information |

</v-clicks>

 
<v-clicks>

<FooterLink text="Official docs MongoDB, JSON and BSON" link="https://www.mongodb.com/resources/basics/json-and-bson" />

</v-clicks>
