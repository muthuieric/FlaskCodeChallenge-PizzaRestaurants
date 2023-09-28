from app import app, db
from models import Pizza, Restaurant, RestaurantPizza
from datetime import datetime

def seed_database():
    with app.app_context():
        try:
            # Create some Pizza instances
            pizza1 = Pizza(id="1", name="Cheese", ingredients="Dough, Tomato Sauce, Cheese", created_at=datetime.utcnow(), updated_at=datetime.utcnow())
            pizza2 = Pizza(id="2", name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni", created_at=datetime.utcnow(), updated_at=datetime.utcnow())

            # Create some Restaurant instances
            restaurant1 = Restaurant(id="1", name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
            restaurant2 = Restaurant(id="2", name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100")

            # Add Pizza instances to Restaurant instances with valid prices
            # Set the price attribute explicitly for each RestaurantPizza instance
            restaurant_pizza1 = RestaurantPizza(restaurant=restaurant1, pizza=pizza1, price=15)
            restaurant_pizza2 = RestaurantPizza(restaurant=restaurant1, pizza=pizza2, price=20)
            restaurant_pizza3 = RestaurantPizza(restaurant=restaurant2, pizza=pizza1, price=18)

            # Commit changes to the database
            db.session.add_all([pizza1, pizza2, restaurant1, restaurant2, restaurant_pizza1, restaurant_pizza2, restaurant_pizza3])
            db.session.commit()

        except Exception as e:
            print(f"Error: {e}")
            db.session.rollback()

if __name__ == '__main__':
    seed_database()
