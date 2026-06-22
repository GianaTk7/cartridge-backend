from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name: str
    brand: str
    description: str
    price: float
    originalPrice: float
    image: str  
    stock: int
    category: Optional[str] = None
    Tags: Optional[str] = None
    createdAt: datetime = datetime.now()
    updatedAt: Optional[datetime] = None