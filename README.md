# numbertotext
[![codecov](https://codecov.io/gh/Sylvaner/NumberToText/branch/main/graph/badge.svg?token=Qc5mixBbjj)](https://codecov.io/gh/Sylvaner/NumberToText)
[![action](https://github.com/Sylvaner/numbertotext/actions/workflows/workflow.yml/badge.svg)](https://github.com/Sylvaner/numbertotext/actions)

Python module that convert numbers to text.

Available language : 
* French

# Usage

```python
from numbertotext import numbertotext

text_number = numbertotext(123456)
print(text_number)
```

Result: 
```
cent-vingt-trois-mille-quatre-cent-cinquante-six
```

# Development
## Testing

```
cd test
python tests.py
```

