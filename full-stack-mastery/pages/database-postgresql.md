# Database - PostgreSQL

Index 
 
data structure assign summarize give you shortcut
like in library on R we will have Rowling
handbook, phone book

indexes speed filter and sort
can also help other operations
right index for the job
indexes cost on insert/update on DELETE?

Index is a data structure that improves the speed of data retrieval operations on a database table at the cost of additional writes and storage space to maintain the index data structure.

https://www.postgresql.org/docs/current/indexes-types.html

Index Types
B-Tree
LSM-Tree

- B-Tree - self balancing search tree
  Nodes list (low, high) ranges of all of their descendants
  Leaves list (kye) => (page, row ID)
  Leaf pages hold link to next leaf page
- Hash Tables - fast lookups, excelent for == matching, smaller storage, one field only
- GIN - Generalized Inverse Index - supports full-text search, use "tsvector" type
- BRIN - Block Range Index - for large tables, store min and max values for each page, tiny storage needs
- GiST 
- SP-GiST


TANSTAAFL - There Ain't No Such Thing As A Free Lunch

Indexing cost memory(RAM), disk space, and time to maintain the index data structure.
Updating indexes makes writes slower.
Insert, updated, and delete operations on the table will be slower because the indexes also need to be updated.

Partial Indexes

Remember to maintain indexes.

Performance

There are different types of scan nodes for different table access methods: sequential scans, index scans, and bitmap index scans. 

EXPLAIN

EXPLAIN VERBOSE 

EXPLAIN ANALYZE

EXPLAIN (ANALYZE, BUFFERS)

wehen we ask for query with only id 
it's the primary key, it the fastest way to get the data


name is in the heap

what is heap?

heap rows


query with `like` is slow the worst case for query
`select` * next example
<!-- DOUBLE CHECK when we use `like` with `%` at the beginning of the string -->
like is not using index


The process I recommend
1) Run on a realistic data set
  * Run on a realistic data set, 
  * Number of rows is especially important
  * Affect join/sort/scan choices
2) Make use of the EXPLAIN parameters
  * In this case, less is not more
    ```sql
    EXPLAIN (ANALYZE, BUFFERS, SETTINGS, VERBOSE)
    SET track_io_timing = ON;
    ```
3) Start at the end
  * Planning time, Trigger time, JIT(just-in-time) total time  https://www.postgresql.org/docs/current/jit-decision.html
  * Read plans bottom-to-top (well, inside-out)
4) Work out what the most expensive parts are
  * Most stats inclusive of chidren, and per-loop
5) Only then, think about how to speed it up
  * Common trap: looking for issues first 

Tools:
* explain.depesz.com
* explain.dalibo.com
* pgmustard.com
* pgAdmin
* OmniDB
* Tensor

Watch: 

* Database Indexing Explained (with PostgreSQL) - Hussein Nasser https://www.youtube.com/watch?v=-qNSXK7s7_w

* A beginners guide to EXPLAIN ANALYZE – Michael Christofides https://www.youtube.com/watch?v=31EmOKBP1PY

* PostgreSQL Indexing : How, why, and when. Curtis Maloney https://www.youtube.com/watch?v=clrtT_4WBAw

More: 
<!-- CHATGPT XD? Josh Berkus - PostgreSQL Performance for Humans -->
postgresql.org/docs/current/using-explain.html
Josh Berkus Explaning EXPLAIN
ogmustard.com/docs/expalin


Commands:

- SELECT
- INSERT
- UPDATE
- DELETE
- CREATE
- ALTER
- DROP
- TRUNCATE
- RENAME
- JOIN
- UNION
- WHERE
- ORDER BY
- GROUP BY
- HAVING
- LIMIT
- OFFSET
- IN
- BETWEEN
- LIKE
- IS NULL
- IS NOT NULL
- EXISTS
- NOT EXISTS
- ANY
- ALL
- UNIQUE
- PRIMARY KEY
- FOREIGN KEY
- CHECK
- DEFAULT
- INDEX
- AUTO_INCREMENT
- EXPLAIN 
- VACUUM
- CONSTRAINT
- TRIGGER
- VIEW
- CURSOR
- STORED PROCEDURE
- FUNCTION
- SUBQUERY
- UNION
- UNION ALL
- INTERSECT
- COMMIT
- COUNT
- SUM
- AVG
- MIN
- MAX
-   

TODO:

* Replication

* Partitioning

* Sharding

* Transactions

* Scalability - Vertical and Horizontal

* BATCH PROCESSING VS STREAM PROCESSING

* Rollback

* Commit

* Schema design - best practices
  * Naming conventions

* Data types

* Normalization

* Denormalization

* Relationships
  
* ACID

  - Atomicity
  - Consistency
  - Isolation
  - Durability





# Schema design - best practices

Best practices for schema design in PostgreSQL:

1. Naming conventions
2. Data types
3. Normalization
4. Denormalization
5. Relationships
6. 