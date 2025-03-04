"""
Utilities for Jupyter notebooks in this project.
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

def setup_notebook_environment():
    """
    Set up the notebook environment with proper path for imports
    and configure display settings.
    """
    # Add the project root to the Python path if not already there
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
        print(f"Added {project_root} to Python path")
    
    # Configure pandas display settings
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.expand_frame_repr', True)
    
    # Configure matplotlib
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['figure.figsize'] = [12, 8]
    
    print("Notebook environment setup complete")

def style_dataframe(df):
    """Apply a consistent style to a DataFrame for display."""
    return df.style.set_properties(**{
        'white-space': 'pre-wrap', 
        'text-align': 'left',
        'font-size': '13px'
    }).set_table_styles([{
        'selector': 'th',
        'props': [('background-color', '#f0f0f0'), ('text-align', 'center')]
    }])
