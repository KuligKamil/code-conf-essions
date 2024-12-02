---
hideInToc: true
---

# Connect to Database

<v-clicks>

```python 
import os

from asyncio import run
from beanie import Document, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

class User(Document):
    name: str
    
async def database_init(document_models: list[Document], clear_database: bool = False) -> None:
    client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))

    await init_beanie(
        database=client.workshop,
        document_models=document_models,
        multiprocessing_mode=True,
    )
    if clear_database:
        await client.drop_database(name_or_database=client.workshop)

if __name__ == "__main__":
    run(database_init(document_models=[User]))
```

<FooterLink text="Documentation Beanie: How to Initialize Connection" link="https://beanie-odm.dev/tutorial/initialization/" />

</v-clicks>

<!--
TODO: add lines to coder
# lines 
# Create Motor client
# To drop database - for easier iterate and test.
# Initialize beanie with the Sample document class and a database
Beanie uses Motor as an async database engine. To initialize previously created documents, you should provide a Motor database instance and a list of your document models to the init_beanie(...) function, as it is shown in the example:
Function **`init_beanie`** also supports the parameters named:
* `allow_index_dropping: bool = False` - If you manage the indexes by yourself, when the parameter is set to`True`, indexes will be dropped.
* `recreate_views: bool = False` - If you want to use virtual views this parameter should be set to `True` *(aggregation pipelines stored in MongoDB that act as collections for reading operations)*.
* `multiprocessing_mode: bool = False` - If multiprocessing mode is set to `True` it will patch the motor client to use process's event loop. -->