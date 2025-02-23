from pydantic import BaseModel, Field
from typing import List, Any, Dict




class Chunks(BaseModel):
    text: str | None    
    vector: List[float] | None = Field(min_length=3072, max_length=3072)
    metadata: Dict[str, Any] | None
    
    class Config:
        from_attributes = True  
