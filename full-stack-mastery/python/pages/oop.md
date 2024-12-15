```python

The super() function does much more than just search the parent class for a method or an attribute. It traverses the entire class hierarchy for a matching method or attribute. If you aren’t careful, super() can have surprising results.

```

with class we create namespace where attributes and methods live

what scope is in the class


<!-- class Person:  -->


Name Mangling
Another naming convention that you can see and use in Python classes is to add two leading underscores to attribute and method names. This naming convention triggers what’s known as name mangling.

Name mangling is an automatic name transformation that prepends the class’s name to the member’s name, like in _ClassName__attribute or _ClassName__method. This transformation results in name hiding. In other words, mangled names aren’t available for direct access and aren’t part of a class’s public API.

For example, consider the following sample class:

```python

>>> class SampleClass:
...     def __init__(self, value):
...         self.__value = value
...     def __method(self):
...         print(self.__value)
...

>>> sample_instance = SampleClass("Hello!")
>>> vars(sample_instance)
{'_SampleClass__value': 'Hello!'}

>>> vars(SampleClass)
mappingproxy({
    ...
    '__init__': <function SampleClass.__init__ at 0x105dfd4e0>,
    '_SampleClass__method': <function SampleClass.__method at 0x105dfd760>,
    '__dict__': <attribute '__dict__' of 'SampleClass' objects>,
    ...
})

>>> sample_instance = SampleClass("Hello!")
>>> sample_instance.__value
Traceback (most recent call last):
    ...
AttributeError: 'SampleClass' object has no attribute '__value'

>>> sample_instance.__method()
Traceback (most recent call last):
    ...
AttributeError: 'SampleClass' object has no attribute '__method'

```