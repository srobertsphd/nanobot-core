from pydantic import BaseModel, conlist
from typing import List


class ChunkMetadata(BaseModel):
    filename: str
    page_numbers: List[int]
    title: str
    
    class Config:
        from_attributes = True

class Chunks(BaseModel):
    text: str
    vector: conlist(float, min_items=1536, max_items=1536)
    metadata_id: int
    
    class Config:
        from_attributes = True  
