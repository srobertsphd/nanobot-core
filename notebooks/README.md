# Analysis Notebooks

This directory contains Jupyter notebooks for data analysis and experimentation.

## Using the Notebook Utilities

All notebooks should use the `notebook_utils.py` module to set up the environment properly:


```python
from notebook_utils import setup_notebook_environment

setup_notebook_environment()
```

### Available Utilities

- `setup_notebook_environment()`: Configures the Python path and display settings
- `style_dataframe(df)`: Applies consistent styling to pandas DataFrames

## Notebook Templates

Use `00_template.ipynb` as a starting point for new analysis notebooks.



