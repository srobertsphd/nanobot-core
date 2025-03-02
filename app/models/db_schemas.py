from pydantic import BaseModel, Field, ConfigDict
from typing import List


class ChunkMetadata(BaseModel):
    filename: str
    title: str
    page_numbers: List[int]
    # Add any other optional fields you might want to include
    

class Chunks(BaseModel):
    text: str 
    vector: List[float] = Field(min_length=3072, max_length=3072)
    metadata: ChunkMetadata
    
    model_config = ConfigDict(  # New style
        arbitrary_types_allowed=True
    )
