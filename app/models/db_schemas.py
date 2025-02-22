from pydantic import BaseModel, Field
from typing import List, Annotated


class ChunkMetadata(BaseModel):
    filename: str
    page_numbers: List[int]
    title: str
    
    class Config:
        from_attributes = True

class Chunks(BaseModel):
    text: str
    vector: Annotated[List[float], Field(min_length=1536, max_length=1536)]
    metadata_id: int
    
    class Config:
        from_attributes = True  
