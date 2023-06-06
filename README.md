# python

<details><summary>References</summary>

- [github Python .gitignore file](https://github.com/github/gitignore/blob/main/Python.gitignore)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [pytest doco](https://docs.pytest.org/en/7.3.x/)
- [Pytest | Visual Studio Code](https://www.youtube.com/watch?v=ucjRpS7WCPA)
- [pylint](https://pypi.org/project/pylint/)
- [pylint docs](https://docs.pylint.org/#)
- [How do I automatically fix lint issues reported by pylint?](https://stackoverflow.com/questions/54586757/how-do-i-automatically-fix-lint-issues-reported-by-pylint)
- [Fix pylint errors with autopep8](https://github.com/hhatto/autopep8)
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
- [Python Docstrings](https://www.programiz.com/python-programming/docstrings)
- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
- [8 Levels of Using Type Hints in Python](https://medium.com/techtofreedom/8-levels-of-using-type-hints-in-python-a6717e28f8fd)
- [Documenting Your Code with Python - Overview of Comments, Docstrings and Type Hints](https://www.youtube.com/watch?v=tqKcq5jVeo4)
- [pytest-cov’s documentation](https://pytest-cov.readthedocs.io/en/latest/)
- [pytest-cov pip documentation](https://pypi.org/project/pytest-cov/)
- [How to generate a documentation for Python project using pdoc](https://lucacorbucci.medium.com/how-to-generate-a-documentation-for-python-code-using-pdoc-60f681d14d6e)
- [pylint: Ignore line-too-long for long URLs](https://github.com/pylint-dev/pylint/issues/2178)
- [python modules](https://docs.python.org/3/tutorial/modules.html)

</details>

<details><summary>python commands summary</summary>

```bash
python --version
alias
alias python=`which python3`
pip --version
# pip install -U pytest
pytest -vv
# pip install pytest-cov 
pytest --cov -v
# pip install pylint
pylint */*.py *.py --recursive y
# pip install --upgrade autopep8
# autopep8 --version
# autopep8 * -r -a -v --experimental -d
autopep8 *.py **/*.py --recursive --aggressive --verbose --experimental --diff
# autopep8 * -r -a -v --experimental -i
autopep8 *.py **/*.py --recursive --aggressive --verbose --experimental --in-place
# python -m pydoc utils.cards
# python -m pydoc -k http
python -m pydoc math.pow
# pip install pdoc3
# pdoc --html . --html-dir docs --force
open docs/python/index.html 
python -m doctest -v *.py **/*.py
```

</details>


<details><summary>Making python3 and pip3 the default on mac</summary>

```bash
python --version
# Python 2.7.16
python3 --version
Python 3.9.5
ls -al /usr/local/bin/python3
# lrwxr-xr-x  1 shawfire  admin  42 Mar 16 16:12 /usr/local/bin/python3 -> ../Cellar/python@3.11/3.11.2_1/bin/python3

# To Tell What Shell Your Mac is Using
echo $0
# /bin/bash

which python
# /usr/bin/python

which python3
# /Library/Frameworks/Python.framework/Versions/3.9/bin/python3

alias python=`which python3`
alias
# alias python='/Library/Frameworks/Python.framework/Versions/3.9/bin/python3'

pip --version
# pip 23.1.2 from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pip (python 3.9)

pip3 --version
# pip 23.1.2 from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pip (python 3.9)
```

Add "alias python=`which python3`" to `~/.zshrc` and `~/.bashrc` file

In VS Code select the correct Python interpreter:
Cmd Shift P "python interpreter" and select the python interpreter you want

</details>

<details><summary>pytest</summary>

```bash
python --version
# Python 3.9.5

pip --version
# pip 23.1.2 from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pip (python 3.9)

pytest --version
# bash: pytest: command not found

# Install pytest
pip install -U pytest

# Run pytest
pytest

pytest --version
# pytest 7.3.1

# Display the whole comparison when a test fails with the double verbose flag -vv
pytest -vv
```

</details>

<details><summary>pytest-cov - pytest test coverage</summary>

- [pytest-cov’s documentation](https://pytest-cov.readthedocs.io/en/latest/)
- [pytest-cov pip documentation](https://pypi.org/project/pytest-cov/)

```bash
pip install pytest-cov 
pytest --cov
pytest --cov -v
```

</details>


<details><summary>pylint</summary>

```bash
pylint --version
pip install pylint
pylint --version
# pylint 2.17.4
# astroid 2.15.5
# Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
# [Clang 6.0 (clang-600.0.57)]
pylint --help
pylint --max-line-length=80 utils/cards_test.py

pylint */*.py *.py --recursive y
```

</details>

<details><summary>autopep8 - fixes pylint errors</summary>

- [Fix pylint errors with autopep8](https://github.com/hhatto/autopep8)

```bash
pip --version
# pip 23.1.2 from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pip (python 3.9)
python --version
# Python 3.9.5
pip install --upgrade autopep8
autopep8 --version
# autopep8 2.0.2 (pycodestyle: 2.10.0)
autopep8 -h

autopep8 * --recursive --aggressive --verbose --diff 
# this command is the same as the above
# autopep8 * -r -a -v -d 

# Need to specify the file types *.py **/*.py otherwise *.md files are also targeted
autopep8 *.py **/*.py --recursive --aggressive --verbose --in-place 
# this command is the same as the above
# autopep8 * -r -a -v -i

# fixes pylint lines to long errors with the --experimental flag
autopep8 *.py **/*.py --recursive --aggressive --verbose --experimental --diff
autopep8 *.py **/*.py --recursive --aggressive --verbose --experimental --in-place
```

</details>

<details><summary>autopep8 -h</summary>

```bash
autopep8 -h
usage: autopep8 [-h] [--version] [-v] [-d] [-i] [--global-config filename] [--ignore-local-config] [-r] [-j n] [-p n] [-a] [--experimental] [--exclude globs] [--list-fixes] [--ignore errors] [--select errors] [--max-line-length n] [--line-range line line] [--hang-closing]
                [--exit-code]
                [files ...]

Automatically formats Python code to conform to the PEP 8 style guide.

positional arguments:
  files                 files to format or '-' for standard in

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v, --verbose         print verbose messages; multiple -v result in more verbose messages
  -d, --diff            print the diff for the fixed source
  -i, --in-place        make changes to files in place
  --global-config filename
                        path to a global pep8 config file; if this file does not exist then this is ignored (default: /Users/shawfire/.config/pep8)
  --ignore-local-config
                        don't look for and apply local config files; if not passed, defaults are updated with any config files in the project's root directory
  -r, --recursive       run recursively over directories; must be used with --in-place or --diff
  -j n, --jobs n        number of parallel jobs; match CPU count if value is less than 1
  -p n, --pep8-passes n
                        maximum number of additional pep8 passes (default: infinite)
  -a, --aggressive      enable non-whitespace changes; multiple -a result in more aggressive changes
  --experimental        enable experimental fixes
  --exclude globs       exclude file/directory names that match these comma-separated globs
  --list-fixes          list codes for fixes; used by --ignore and --select
  --ignore errors       do not fix these errors/warnings (default: E226,E24,W50,W690)
  --select errors       fix only these errors/warnings (e.g. E4,W)
  --max-line-length n   set maximum allowed line length (default: 79)
  --line-range line line, --range line line
                        only fix errors found within this inclusive range of line numbers (e.g. 1 99); line numbers are indexed at 1
  --hang-closing        hang-closing option passed to pycodestyle
  --exit-code           change to behavior of exit code. default behavior of return value, 0 is no differences, 1 is error exit. return 2 when add this option. 2 is exists differences.
```

</details>

<details><summary>pydoc</summary>

```bash
python -m pydoc
python -m pydoc pow

# key work examples
python -m pydoc -k http

# python package documentation
python -m pydoc math

# open python documentation in browser on specified port
python -m pydoc -p 8080

# open python documentation in browser on available port
python -m pydoc -b

python -m pydoc utils.cards

# Be careful with pydoc as it could use old python 2.x 
# use python -m pydoc
# especially when using an alias for python3
which pydoc
# /usr/bin/pydoc
which python
# /usr/bin/python
/usr/bin/python --version
# Python 2.7.16
alias
# alias python='/Library/Frameworks/Python.framework/Versions/3.9/bin/python3'
python --version
# Python 3.9.5
```

</details>

<details><summary>pdoc</summary>

[How to generate a documentation for Python project using pdoc](https://lucacorbucci.medium.com/how-to-generate-a-documentation-for-python-code-using-pdoc-60f681d14d6e)

```bash
pip install pdoc3
pdoc --html . --html-dir docs
open docs/python/index.html 
```

</details>

<details><summary>doctest</summary>

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
- [pylint: Ignore line-too-long for long URLs](https://github.com/pylint-dev/pylint/issues/2178)

```bash
python -m doctest -v *.py **/*.py
```

</details>
