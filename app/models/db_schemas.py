from pydantic import BaseModel, Field
from typing import List, Any, Dict




class Chunks(BaseModel):
    text: str
    vector: List[float] = Field(min_length=3072, max_length=3072)
    metadata: Dict[str, Any]
    
    class Config:
        from_attributes = True  
