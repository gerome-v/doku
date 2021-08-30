##How to document Python project using Sphinx and RTD
- This repo is a dummy Python project that illustrates how to generate 
  documenatiton using Sphinx and RTD style theme.

###1. Install the following packages
```bash 
$ pip install -U sphinx sphinx-rtd-theme
```
###2. Create a docs folder. 
   Here is the folder structure of this project.
```
| doku
| ├── docs
| ├── README.md
| └── doku
|     └── data_builder.py
|     └── model_builder.py
|     └── utils.py 
```

###3. Build sphinx related files inside `docs/`. 
```bash
cd docs 
PROJECT_NAME=doku 
AUTHOR=GV
RELEASE=0.1
sphinx-quickstart  --sep -p $PROJECT_NAME -a $AUTHOR -r $RELEASE -l en
```
where doku is your project name. GV is the author name

###4. Edit `conf.py` file by adding these code.
```python
# docs/source/conf.py
import os
import sys
from pathlib import Path
import sphinx_rtd_theme

# Add parent dir to known paths
p = Path(__file__).parents[2]
sys.path.insert(0, os.path.abspath(p))

# Add the following extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme'
]

# Use RTD theme
html_theme = "sphinx_rtd_theme"

```
###5. Automatically generate documentation from your docstrings. 
Make sure your docstrings are legible ([link](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/)). 
   Generate documentation using your docstrings from your 
   Python code.
```bash
$ sphinx-apidoc -f -o ./source ../doku
```

Add modules to `index.rst`
```
# docs/source/index.rst
Welcome to doku's documentation!
================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
```

Update the documentation
```bash
$ make clean && make html
```
That's it! Your documentation is now ready. Using your favorite web browser, 
open `index.html` from `docs/build/html/index.html`. For more information, you 
can check out [Sphinx](https://www.sphinx-doc.org/en/master/contents.html). 



---
---
##### If you also want to generate a pdf version of your documentation. Run:

```bash
make latexpdf
```
You can zip the latex folder `docs/build/latex/` and import it to 
Overleaf then generate the pdf file from there.
