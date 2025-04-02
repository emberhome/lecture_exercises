from pydantic import BaseModel

class RestaurantCreate(BaseModel):
    name: str  # list, dict, datetime, int, float, bool
    cuisine_style: str
    city: str

    class Config:
        orm_mode = True

class Restaurant(RestaurantCreate):
    id: int


    class Config:
        orm_mode = True
