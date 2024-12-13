Concurrency: Multithreading, Multiprocessing, Parallelism

keywords: Event Loop, async/await, threat, task, process, IO Bound, CPU Bound, locks, semaphores, mutex
python: asyncio, GIL
js: callbacks, promises, Web Workers

In Python, variables are dynamically typed, 
allowing you to assign values of different data types
to a variable at different times.


When you assign a value to a variable in Python, what happens behind the scenes?
* The variable points to an object.
* The object is assigned a unique identifier.
  
In Python, when you create a variable, it doesn’t directly store the object. 
Instead, the variable acts as a pointer or reference to the object. 
Each object is created in memory and assigned a unique identifier, which in CPython corresponds to the object’s memory address. 
Multiple variables can reference the same object, meaning they hold the same memory address.

When a variable is reassigned, it points to a new object, and if no other variables reference the original object, 
Python’s garbage collector will reclaim the memory of the orphaned object. 
You can read more about this process in detail in the section on variables holding references to objects.
https://realpython.com/python-variables/#variables-hold-references-to-objects

Concurrency is doing many things at the same time. 
In Python, the multiprocessing module and a pool executor from concurrent.futures does this by having different Python interpreters run on different CPUs. 
In asyncio and threading, Python does this by doing some work on one task while another task is waiting for a response from a slow interface.


TODO: Python when use tread over asnycio

<!-- Python has a Global Interpreter Lock (GIL) that prevents multiple threads from executing Python bytecodes at once. -->

When use in IO Bound asnycio when thraed?


For IO-bound problems, you can use both asyncio and threads, but they are suited for different scenarios. Here is a brief explanation:

asyncio
Use Case: When you have many IO-bound tasks that can be awaited, such as network requests, file I/O, or database queries.
Advantages: Efficiently handles many tasks with a single thread, lower memory usage, and better performance for high-concurrency tasks.
Example: Handling multiple HTTP requests concurrently.
Threads
Use Case: When you have IO-bound tasks that do not support asynchronous operations or when you need to run blocking code.
Advantages: Easier to integrate with existing synchronous code, can run blocking code without blocking the main thread.
Example: Running a blocking library function that does not support async.


import asyncio
import aiohttp

async def fetch_url(session, url):
  async with session.get(url) as response:
    return await response.text()

async def main():
  async with aiohttp.ClientSession() as session:
    urls = ['http://example.com', 'http://example.org']
    tasks = [fetch_url(session, url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())

import threading
import requests

def fetch_url(url):
  response = requests.get(url)
  print(response.text)

urls = ['http://example.com', 'http://example.org']
threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]

for thread in threads:
  thread.start()

for thread in threads:
  thread.join()


  Summary
Use asyncio for high-concurrency IO-bound tasks that support async.
Use threads for IO-bound tasks that do not support async or involve blocking code.