This repository houses intentionally broken or flawed code used as a practical exercise.

The script `pyunsustainable/find_tokens.py` should search a file for strings that approximately match a query token.
Unfortunately, the application does not work as intended.

### Setup

Firstly, clone the repository with:

```
https://github.com/asouthgate/unsustainable-code
```

To install pytest:

```
python -m pip install pytest
```

### Usage

To attempt to run the code:

```
python3 pyunsustainable/find_tokens.py test/example_text_file token
```

### Testing

To attempt to run the tests:

```
pytest test/test_find_tokens.py
```

What happens?

### Making changes

To make a change, open a project file such as `test_find_tokens.py` and make a change. Then:

```
git add test_find_tokens.py
```

Commit the change with:

```
git commit -m 'a meaningful message goes here'
```

What happens?
