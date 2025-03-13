import os
import sys
from pathlib import Path

def generate_tree(startpath, exclude_dirs=None, max_depth=None):
    if exclude_dirs is None:
        exclude_dirs = ['.git', '.venv', '__pycache__', '.pytest_cache', 'node_modules']
    
    for root, dirs, files in os.walk(startpath):
        # Calculate current depth
        level = root.replace(startpath, '').count(os.sep)
        
        # Check if we've reached max depth
        if max_depth is not None and level >= max_depth:
            del dirs[:]  # Clear dirs to prevent further recursion
            continue
            
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        # Print directory with indentation
        indent = '│   ' * level
        print(f"{indent}├── {os.path.basename(root)}/")
        
        # Print files with indentation
        subindent = '│   ' * (level + 1)
        for f in files:
            print(f"{subindent}├── {f}")

if __name__ == "__main__":
    path = "."  # Default to current directory
    depth = None  # Default to unlimited depth
    
    if len(sys.argv) > 1:
        path = sys.argv[1]
    if len(sys.argv) > 2:
        depth = int(sys.argv[2])
        
    print(f"{os.path.basename(os.path.abspath(path))}/")
    generate_tree(path, max_depth=depth)
