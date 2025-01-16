# python vs javascript

## Difference

* tabs sense in python, braces in javascript
* javascript is prototype based, python is class based
* 
* python is strongly typed, javascript is weakly typed
* python have 1 thread - GIL, js 1 thread
* js have web workers
* to convert string to int in python use int(), in js use parseInt()
* declared variable python nothoing, js var, let, const
* python def, js function
* Typesceript is statically typed to compile to js, more advanced than in Python


As you’ve already learned, Python provides a rich set of immutable built-in data types. Numeric types, such as int, float, and complex, can hold single-item objects that you can’t mutate during your code execution. These types are immutable. In Python, the bool class, which supports the Boolean type, is a subclass of int. So, this type is also immutable.

When it comes to collection types, str, bytes, and tuple are also immutable even though they can store multiple-item values.

https://realpython.com/python-mutable-vs-immutable-types/#immutable-built-in-data-types-in-python


| Category                 | Python                                               | JavaScript                                                             |
| ------------------------ | ---------------------------------------------------- | ---------------------------------------------------------------------- |
| **Mutable Objects**      | `list`, `dict`, `set`, `bytearray`                   | `Object`, `Array`, `Set`, `Map`                                        |
| **Immutable Objects**    | `int`, `float`, `complex`, `str`, `tuple`, `frozenset`, `bytes` | `number`, `string`, `boolean`, `null`, `undefined`, `symbol`, `bigint` |
| **Strings**              | Immutable                                            | Immutable                                                              |
| **Arrays/Lists**         | Mutable                                              | Mutable                                                                |
| **Objects/Dictionaries** | Mutable                                              | Mutable (can use `Object.freeze()`)                                    |
| **Primitives**           | Immutable                                            | Immutable                                                              |



| Feature              | Python                          | JavaScript                                     |
| -------------------- | ------------------------------- | ---------------------------------------------- |
| **Block Scope**      | No block scope                  | Block scope with `let` and `const`             |
| **Function Scope**   | Default for local variables     | `var` has function scope                       |
| **Global Variables** | Requires `global` keyword       | Can be modified by default                     |
| **Enclosing Scope**  | Use `nonlocal` for modification | Free access and modification                   |
| **Hoisting**         | No hoisting                     | Hoisting for `var` (limited for `let`/`const`) |



w pythonie jak cos jest przekazywane do funkcji to przez wartosc czy referencje?
ChatGPT said:
ChatGPT
W Pythonie argumenty funkcji są przekazywane przez obiekt. Nie jest to stricte przekazywanie przez wartość ani przez referencję w tradycyjnym sensie, który można spotkać w językach takich jak C czy C++.

Jak to działa?
Przekazywany jest wskaźnik (referencja) do obiektu.
Jeśli zmienisz zawartość obiektu mutable (np. listy, słowniki), to zmiany będą widoczne poza funkcją.
Jeśli jednak przypiszesz nową wartość do zmiennej wewnątrz funkcji, to tworzysz nową lokalną referencję (nie zmieniasz oryginalnego obiektu).
Przykłady:
Przekazywanie obiektów niemutowalnych (immutable), takich jak liczby, stringi, tuple:
python
Copy code
def zmien(a):
    a = 10
    print("Wewnątrz funkcji:", a)

x = 5
zmien(x)
print("Na zewnątrz funkcji:", x)
Wynik:

yaml
Copy code
Wewnątrz funkcji: 10
Na zewnątrz funkcji: 5
Tutaj a wewnątrz funkcji jest nową zmienną, która wskazuje na nową wartość. Oryginalny x pozostaje niezmieniony.
Przekazywanie obiektów mutowalnych (mutable), takich jak listy:
python
Copy code
def zmien(l):
    l.append(4)
    print("Wewnątrz funkcji:", l)

lista = [1, 2, 3]
zmien(lista)
print("Na zewnątrz funkcji:", lista)
Wynik:

less
Copy code
Wewnątrz funkcji: [1, 2, 3, 4]
Na zewnątrz funkcji: [1, 2, 3, 4]
W tym przypadku zmiany wewnątrz funkcji są widoczne na zewnątrz, ponieważ obiekt lista jest mutowalny, a operacja .append() modyfikuje jego zawartość.
Podsumowanie:
Python przekazuje referencje do obiektów, ale zachowanie zależy od tego, czy obiekt jest mutable (mutowalny) czy immutable (niemutowalny).
Immutable: Nowe przypisania tworzą nową referencję.
Mutable: Modyfikacja zawartości obiektu wewnątrz funkcji zmienia oryginalny obiekt.





You said:
jak to wyglada w JS?
 
W JavaScript sposób przekazywania argumentów do funkcji działa podobnie jak w Pythonie, ale warto rozróżnić przypadki w zależności od typu wartości:

Typy prymitywne (przekazywanie przez wartość)
Typy złożone (obiekty i tablice - przekazywanie przez referencję do obiektu)
Typy prymitywne (przekazywanie przez wartość)
Typy prymitywne w JavaScript to:

number, string, boolean, null, undefined, symbol, bigint.
Przy przekazywaniu ich do funkcji kopiowana jest wartość. Zmiana zmiennej wewnątrz funkcji nie wpływa na oryginalną wartość.

Przykład:
javascript

function zmien(x) {
    x = 10;
    console.log("Wewnątrz funkcji:", x);
}

let a = 5;
zmien(a);
console.log("Na zewnątrz funkcji:", a);
Wynik:

yaml
Copy code
Wewnątrz funkcji: 10
Na zewnątrz funkcji: 5
Tutaj x to lokalna kopia wartości a. Zmiana x nie wpływa na oryginalną zmienną a.
Typy złożone (przekazywanie przez referencję do obiektu)
Typy złożone, takie jak obiekty i tablice, są przekazywane do funkcji jako referencje. Nie jest to jednak "czyste" przekazywanie przez referencję, jak w C++ — jest to bardziej przekazywanie referencji do wartości.

Oznacza to, że jeśli zmodyfikujesz zawartość obiektu lub tablicy wewnątrz funkcji, zmiany będą widoczne na zewnątrz. Natomiast przypisanie nowej wartości do zmiennej wewnątrz funkcji nie zmieni oryginalnego obiektu.

Przykład - modyfikacja zawartości obiektu:
javascript
Copy code
function zmien(obj) {
    obj.value = 10;
    console.log("Wewnątrz funkcji:", obj);
}

let myObj = { value: 5 };
zmien(myObj);
console.log("Na zewnątrz funkcji:", myObj);
Wynik:

css
Copy code
Wewnątrz funkcji: { value: 10 }
Na zewnątrz funkcji: { value: 10 }
Zmodyfikowaliśmy właściwość obiektu myObj, co wpłynęło na oryginalny obiekt.
Przykład - przypisanie nowej wartości:
Jeśli przypiszesz nową wartość do zmiennej wewnątrz funkcji, oryginalny obiekt pozostanie nietknięty.

javascript
Copy code
function zmien(obj) {
    obj = { value: 10 }; // Przypisujemy nowy obiekt
    console.log("Wewnątrz funkcji:", obj);
}

let myObj = { value: 5 };
zmien(myObj);
console.log("Na zewnątrz funkcji:", myObj);
Wynik:


Wewnątrz funkcji: { value: 10 }
Na zewnątrz funkcji: { value: 5 }
W tym przypadku obj zaczęło wskazywać na nowy obiekt wewnątrz funkcji, ale oryginalna zmienna myObj pozostaje nietknięta.
Podsumowanie:
Typy prymitywne:

Przekazywane przez wartość.
Zmiana zmiennej wewnątrz funkcji nie wpływa na oryginał.
Typy złożone (obiekty, tablice):

Przekazywane przez referencję do wartości (wskaźnik do obiektu).
Modyfikacja zawartości obiektu/tablicy zmienia oryginalną wartość.
Przypisanie nowej wartości do zmiennej nie zmienia oryginału.
JavaScript nie pozwala na stricte "przekazywanie przez referencję", ale umożliwia operowanie na obiektach za pomocą referencji, co może przypominać przekazywanie przez referencję w innych językach.


# what is the difference between strong and weak typing?

Strong typing means that the type of a variable is checked at compile-time, and an implicit conversion will not be performed. Weak typing means that a language will allow a variable to be coerced into another type and will perform implicit type conversion.







similar

* dynamically typed languages

# args & kwargs in python

args and kwargs are used in Python to pass a variable number of arguments to a function.

args is used to send a non-keyworded variable length argument list to the function. Here’s an example:

```python

def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')

```

This produces the following result:

```python   
first normal arg: yasoob
another arg through *argv: python
another arg through *argv: eggs
another arg through *argv: test
```

kwargs allows you to pass keyworded variable length of arguments to a function. You should use **kwargs if you want to handle named arguments in a function. Here is an example to get you going with it:

```python
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))   


greet_me(name="yasoob", age=23)
```



