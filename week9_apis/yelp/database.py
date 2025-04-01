from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models

engine = create_engine('sqlite:///./restaurants.sqlite')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

if __name__ == "__main__":
    with SessionLocal() as db:
        # restaurants = db.query(models.Restaurant)\
        #     .offset(50)\
        #     .limit(100)\
        #     .all()
        # [print(r.name) for r in restaurants]

        # restaurants = db.query(models.Restaurant)\
        #     .where(models.Restaurant.cuisine_style=='Italian', models.Restaurant.city=='Paris')\
        #     .all()
        # [print(r.name) for r in restaurants]


        # restaurants = db.query(models.Restaurant)\
        #     .filter(models.Restaurant.name.ilike('t%'))\
        #     .all()
        # [print(r.name) for r in restaurants]


        # new_restaurants = models.Restaurant(name = 'Tantura', cuisine_style = 'Middle Eastern', city = 'Lisbon', id=943)
        # db.add(new_restaurants)
        # db.commit()

        # db.delete(new_restaurants)
        # db.commit()

        # restaurants = db.query(models.Restaurant)\
        #     .limit(1000)\
        #     .all()
        # [print(r.id) for r in restaurants]

        # for r in restaurants:
        #     try:
        #         print(r.id)
        #     except:
        #         print(r)



        restaurants = db.query(models.Restaurant)\
            .filter(models.Restaurant.name=='Tantura')\
            .all()
        [print(r.name) for r in restaurants]

        # for r in restaurants:
        #     try:
        #         print(r.name)
        #     except:
        #         print(r)
        #[print(r.name) for r in restaurants]
        # print("Restaurants returned:", restaurants)
        # #print(db.is_active)  # Should print True if the session is active
