
https://realpython.com/python-formatted-output/#f-string-formatting


```python 

lang = "Python"

     👇         👇
f"{{ {lang} }}"
# '{ Python }'

salary_sigma_programmer = 1_000_000
print(f"{salary_sigma_programmer:,}")
print(f"{salary_sigma_programmer:_}")
# "{0:,.2f}".format(1234567.89)
print(f"{1234567.89:,.2f}")

```