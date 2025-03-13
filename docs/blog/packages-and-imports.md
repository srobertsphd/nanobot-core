This is a good reference for importing packages:

https://www.youtube.com/watch?v=VEbuZox5qC4

Tech with Tim


from the chunking.py file in the document_conversion folder, I want to import the Chunks and ChunkMetadata classes from the models.db_schemas module.

```python
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from models.db_schemas import Chunks, ChunkMetadata
```


1. os.path.abspath(__file__):
This gets the absolute path of the current file (chunking.py).
2. os.path.dirname():
Called twice to move up two directory levels, reaching the root of your project (nanobot-poc).
3. sys.path.append(parent_dir):
Adds the parent directory to sys.path, which is the list of directories Python searches for modules.
By including the parent directory, Python can now find models.db_schemas because models is a sibling directory to document_conversion.
4. Import Statement:
With the parent directory in sys.path, the import from models.db_schemas import Chunks, ChunkMetadata works because Python can now locate the models directory.


This method effectively adjusts the module search path at runtime, allowing you to import modules from sibling directories.


