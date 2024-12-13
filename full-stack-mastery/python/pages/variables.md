# What happens when you use the del statement on a variable in Python?
It removes the variable’s name from the current scope. https://realpython.com/python-variables/#deleting-variables-from-their-scope

When you use the del statement on a variable in Python, it removes the reference to that variable from its scope. If you try to access that variable afterward, you’ll get a NameError because the variable no longer exists in the scope. It’s important to note that while del removes the reference, it doesn’t necessarily free the memory immediately. Python’s garbage collector will reclaim the memory when there are no more references to the object.

You can read more about deleting variables from their scope in the section on deleting variables from their scope.
TODO: what will be if you delete from local scope and varialbe is in global?
