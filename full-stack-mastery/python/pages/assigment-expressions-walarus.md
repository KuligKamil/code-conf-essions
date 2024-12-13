Assignment expressions in Python, which use the walrus operator, allow you to assign a value to a variable and use it in an expression simultaneously. This can help avoid repeating function calls, such as input(), by assigning and evaluating the result within a single line. For example:

while (line := input("Type some text: ")) != "stop":
    print(line)



https://realpython.com/python-variables/#assignment-expressions
They allow you to assign a value and use it in a conditional at the same time.
:=