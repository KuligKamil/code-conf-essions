# Garbage collector 


In Python, when you create a variable, it doesn’t directly store the object.
Instead, the variable acts as a pointer or reference to the object.
Each object is created in memory and assigned a unique identifier, which in CPython corresponds to the object’s memory address.
Multiple variables can reference the same object, meaning they hold the same memory address.

When a variable is reassigned, it points to a new object, and if no other variables reference the original object,
Python’s garbage collector will reclaim the memory of the orphaned object.