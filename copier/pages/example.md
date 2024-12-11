layout: two-cols
---
# Example

##

<v-clicks>

Use strategy design pattern for complex mathematicians strategies.

Example `Magic` strategy.

* implementation for `magic_strategy.py` in src/strategies folder

* test file for `test_magic_starategy.py` in test folder

* update `readme.md`
* 
https://refactoring.guru/design-patterns/strategy/python/example

</v-clicks>


::right::

<v-clicks>

```python
from abc import ABC, abstractmethod
from typing import List

class Strategy(ABC):

    @abstractmethod
    def do_algorithm(self, data: List):
        pass
```

```python 
# magic_strategy.py

class MagicStrategy(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)
```

How to do it with Copier?


</v-clicks>


---

📁 .strategy_template

├── 📄 copier.yml <- questions for new strategy

├── 📁 src/strategies/`{{name}}`_strategy.py.jinja

├── 📁 tests/test_`{{name}}`_strategy .py.jinja
