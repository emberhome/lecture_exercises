from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import schemas, models
from database import SessionLocal

app = FastAPI()

# db = [{"name": "Chez Justine", "cuisine_style": "French", "city": "Paris"},
#       {"name": "L'Alicheur", "cuisine_style": "Asian", "city": "Paris"}] no longer need dummy data, using SQL lite database instead

def get_db():
    "helper function which opens a connectionn to the SQL database and closes connection at the end of API call"
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

##GET: reading existing data
@app.get('/restaurants',response_model=List[schemas.Restaurant])
def get_restaurants(db: Session = Depends(get_db)):
    return db.query(models.Restaurant).all()



# #POST: adding new data
@app.post('/restaurants',response_model=schemas.Restaurant)
def create_restaurant(restaurant: schemas.RestaurantCreate,db: Session = Depends(get_db)):
    new_restaurant = models.Restaurant(**restaurant.dict())
    db.add(new_restaurant)  # Add to session
    db.commit()  # Commit transaction to save to the database
    db.refresh(new_restaurant)  # Refresh to get generated id
    return new_restaurant  # Return the created restaurant
