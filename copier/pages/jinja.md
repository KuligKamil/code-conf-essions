---
hideInToc: true
---

# Jinja2

Powerful templating engine 

Allowing you to generate HTML, python(py) other files formats with dynamic data.

<!-- ::right:: -->

<v-clicks>

`{{ ... }}` for Expressions to print to the template 


```python
import jinja2

environment = jinja2.Environment()
template = environment.from_string("Hello, {{ name }}!")
name = "Python Summit"
template.render(name=name)
```

`Hello, Python Summit!`

`{% ... %}` for Statements to control the logic of the template


```python
template = environment.from_string("Presentation is a {% if name %}SUCCESS{% else %}FAILURE{% endif %}.")
template.render(name=name)
```

`Presentation is a SUCCESS.`

</v-clicks>