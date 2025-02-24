from pydantic import BaseModel, Field, ConfigDict
from typing import List, Any, Dict



class Chunks(BaseModel):
    text: str | None    
    vector: List[float] | None = Field(min_length=3072, max_length=3072)
    metadata: Dict[str, Any] | None
    
    model_config = ConfigDict(  # New style
        arbitrary_types_allowed=True
    )
