result = (1.2).as_integer_ratio()

print(result)


# The built-in float type in Python includes several methods. For instance, the method 
# .as_integer_ratio()
#  returns a pair of integers whose ratio is exactly equal to the original float. Another method, 
# .is_integer()
# , checks if the float is an integer and returns 
# True
#  if it is.

# Additionally, the 
# .hex()
#  method converts a float to a hexadecimal string, and 
# .fromhex()
#  does the reverse by creating a float from a hexadecimal string.


# The float type in Python has several useful methods for different purposes:

# .as_integer_ratio() returns a tuple of two integers that represent the float as a fraction.
# .is_integer() checks if the float is an integer (i.e., no fractional part).
# .hex() provides a hexadecimal string representation of the float.
# .fromhex() constructs a float from a hexadecimal string.
# These methods are particularly useful in scenarios where precision and specific representations of floating-point numbers are crucial, such as in scientific computations.

# Learn more about these methods and how to use them effectively in Python in the Floating-Point Methods section.

# https://realpython.com/python-data-types/#floating-point-methods



# bytes is immutable, while bytearray is mutable.


# n Python, the bytes type is an immutable sequence of bytes, meaning once a bytes object is created, its content can’t be changed. On the other hand, bytearray is a mutable sequence of bytes, allowing modifications to its content after creation.

# You can learn more about these types and how to use them in the section on bytes and bytearrays.

# What prefix do you need to use to define a bytes literal in Python?
# b


# When using the bytes() function to convert a string into a bytes object, you must provide a character encoding, such as "utf-8". If you omit the encoding, Python will not know how to convert the string and will raise a TypeError.

# For example:

# >>> bytes("Hello, World!", encoding='utf-8')
# b'Hello, World!'
# >>> bytes("Hello, World!")
# Traceback (most recent call last):
#     ...
# TypeError: string argument without an encoding
# To learn more about the bytes() function, check out the section on the Built-in bytes() function.


# why I want to use bytes
# Using bytes in Python can be beneficial for several reasons:

# Binary Data Handling:

# When working with binary data, such as files, images, or network packets, you need to use bytes to read, write, and manipulate the data.
# Encoding and Decoding:

# Converting strings to bytes is essential for encoding text data into a specific format (e.g., UTF-8) and decoding it back to a string. This is particularly useful when dealing with data transmission or storage.
# Performance:

# Operations on bytes objects can be more efficient than on strings, especially when dealing with large amounts of data or performing low-level data manipulation.
# Interfacing with External Systems:

# Many external systems and libraries (e.g., network protocols, file formats, cryptographic functions) require data to be in byte format. Using bytes ensures compatibility with these systems.
# Memory Management:

# bytes objects are immutable, which can lead to better memory management and reduced risk of unintended data modification.
# Example Use Cases
# File I/O: Reading and writing binary files (e.g., images, executables).
# Network Communication: Sending and receiving data over sockets.
# Data Serialization: Encoding data for storage or transmission (e.g., JSON, XML).
# Cryptography: Encrypting and decrypting data using cryptographic algorithms.
# By understanding and utilizing bytes, you can effectively handle various types of data and ensure your programs are robust and efficient.



# bool is a subclass of int