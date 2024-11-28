---
hideInToc: true
---

# Connect to Database

```python 
import os

from asyncio import run
from beanie import Document, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient


async def database_init(document_models: list[Document], clear_database: bool = False) -> None:
    # Create Motor client
    client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))

    # Initialize beanie with the Sample document class and a database
    await init_beanie(
        database=client.workshop,
        document_models=document_models,
        multiprocessing_mode=True,
    )
    # To drop database - for easier iterate and test.
    if clear_database:
        await client.drop_database(name_or_database=client.workshop)

run(database_init(document_models=[Task, User]))
```


*[Documentation for beanie initialization.](https://beanie-odm.dev/tutorial/initialization/)*

<!-- 

Function **`init_beanie`** also supports the parameters named:
* `allow_index_dropping: bool = False` - If you manage the indexes by yourself, when the parameter is set to`True`, indexes will be dropped.
* `recreate_views: bool = False` - If you want to use virtual views this parameter should be set to `True` *(aggregation pipelines stored in MongoDB that act as collections for reading operations)*.
* `multiprocessing_mode: bool = False` - If multiprocessing mode is set to `True` it will patch the motor client to use process's event loop. -->