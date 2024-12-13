https://realpython.com/python-scope-legb-rule/#using-enclosing-scopes-as-closures


LEGB

Local or Function
Enclosing or Nonlocal or Nested Function
  * Closures
Global or Module
Built-in



The concept of 
scope
 determines the visibility of a 
variable
 within your code. In Python, you might encounter up to four different scopes, represented by the LEGB acronym: 
local, enclosing, global, and built-in.

Why not use Global Scope?

Global variables are available to all functions, which can lead to unintended consequences. For example, if you have a global variable with the same name as a local variable, the function will use the local variable. This can lead to bugs that are difficult to track down.