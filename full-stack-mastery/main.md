Fullstack improvements repo 

TODO: 
* List - so dropdown list and save result - for interviews
* Do templates for different languages

Different groups knowledge Must Should Okey Perfect

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


https://realpython.com/python-variables/#assignment-expressions
They allow you to assign a value and use it in a conditional at the same time.
:=


Assignment expressions in Python, which use the walrus operator, allow you to assign a value to a variable and use it in an expression simultaneously. This can help avoid repeating function calls, such as input(), by assigning and evaluating the result within a single line. For example:

while (line := input("Type some text: ")) != "stop":
    print(line)


# What happens when you use the del statement on a variable in Python?
It removes the variable’s name from the current scope. https://realpython.com/python-variables/#deleting-variables-from-their-scope

When you use the del statement on a variable in Python, it removes the reference to that variable from its scope. If you try to access that variable afterward, you’ll get a NameError because the variable no longer exists in the scope. It’s important to note that while del removes the reference, it doesn’t necessarily free the memory immediately. Python’s garbage collector will reclaim the memory when there are no more references to the object.

You can read more about deleting variables from their scope in the section on deleting variables from their scope.
TODO: what will be if you delete from local scope and varialbe is in global?


The concept of 
scope
 determines the visibility of a 
variable
 within your code. In Python, you might encounter up to four different scopes, represented by the LEGB acronym: 
local, enclosing, global, and built-in.


Authentication vs Authorization
Decorators and generators
Async python


Decorator vs ContextManger (with)
__enter__ __exit__

Profiling code (cProfile, memory_profiler) PerformanceAndOptimization
Optimizing with Cython, PyPy

Microservices architecture

Dependency Injection
https://lagom-di.readthedocs.io/en/latest/
"If you are looking for an idea to write a library that could benefit hashtag#python community, please write a decent dependency injection container 🙏

Just joking. We have too many of them already. Worse, they often don't provide the basic features you'd expect from a dependency injection container. One day on Reddit I found out that two new were announced nearly at the same time and one of them hasn't had scopes support.

On top of this, many teams are writing their own implementations. 🙈

I hope we'll see 1-3 libraries taking over most of the market soon.

The one I like the most is called Lagom https://lnkd.in/dr6m56QF 
It requires little configuration, has integrations with many frameworks and does not require code modification, so it does not litter there.
DISCLAIMER: I recently made a small contribution to that library.

An interesting alternative is dishka https://lnkd.in/d8uQ9x4r I haven't used it yet but seems to be only slightly more verbose.

Any other DI container you use and can recommend?

PS: Please don't rely on the one that ships with FastAPI, it prevents code reuse and hinders testing"
https://www.linkedin.com/posts/sebastianbuczynski_lagom-dependency-injection-container-activity-7268271574493843456-l-Qk?utm_source=share&utm_medium=member_desktop

Which data structures? itertools and functools
Collections (namedtuple, deque, Counter)
Pub Sub

Debugging techniques and tools (pdb, logging)






Mocking and patching

Class
Metaclasses
Design patterns
MRO
Keywords
Basic type in python 
SDLC

Authentication vs authorization

Authentication and authorization are two distinct processes used in security:

- **Authentication**: This process verifies the identity of a user or service. It's about confirming that someone is who they claim to be. Common methods include passwords, biometrics, and security tokens.

- **Authorization**: This process determines what an authenticated user or service is allowed to do. It's about granting permissions to access resources or perform actions. Authorization typically involves roles and permissions.

In summary, authentication is about verifying identity, while authorization is about granting access rights.

There are several ways to perform authentication:

* Password-based Authentication: Users provide a username and password to verify their identity.

* Multi-Factor Authentication (MFA): Combines two or more independent credentials (e.g., password and a security token).

* OAuth: A token-based authentication framework that allows applications to access resources on behalf of a user.

* JWT (JSON Web Tokens): A compact, URL-safe means of representing claims to be transferred between two parties.

* SSO (Single Sign-On): Allows users to authenticate once and gain access to multiple systems without re-entering credentials.

* Biometric Authentication: Uses unique biological traits (e.g., fingerprints, facial recognition) to verify identity.

* SSH Keys: Uses cryptographic keys for authenticating users and machines in SSH protocol.

Each method has its own use cases and security implications.

Authorization can be implemented in various ways depending on the requirements of your application. Here are some common methods:

Role-Based Access Control (RBAC): Define roles within your application, each with specific permissions, and assign these roles to users.

Attribute-Based Access Control (ABAC): Use attributes (e.g., user, resource, environment) to define and enforce access policies.

Access Control Lists (ACLs): Maintain a list of permissions attached to objects specifying which users or system processes can access objects.

OAuth Scopes: Use OAuth scopes to define the level of access granted to third-party applications.

Policy-Based Access Control (PBAC): Create and manage policies that define the rules for access control.

These methods can be used individually or in combination to enforce fine-grained access control in your application.



The OAS REST API exposes functionality for reading and writing real-time and historical Tag Data, Trend Data, and Alarms. Additionally, the API can be used for managing OAS Server configurations. All operations require an authenticated session.



GIL is mutex, that allows only one thread at time to execute python bytecode


![Alt text](image.png)
Let's go deeper in async. Exceptions handling, pubsub pattern and how to manage back pressure.



https://www.youtube.com/watch?v=GpqAQxH1Afc


ADR PROCESS
Onboarding Docs


AWS
Lambda


Event Brige
Steep Functions


Debbugger 
Error mesage
whart Error I know 

CORS errors 
waht to logout

https://learnxinyminutes.com/docs/python/