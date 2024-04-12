from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

with app.app_context():
    # Delete all rows in tables
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    # Seed restaurants
    restaurant1 = Restaurant(name='Dominion Pizza', address='Good Italian, Ngong Road, 5th Avenue')
    restaurant2 = Restaurant(name='Pizza Hut', address='Westgate Mall, Mwanzi Road, Nrb 100')

    db.session.add(restaurant1)
    db.session.add(restaurant2)
    db.session.commit()  # Commit the restaurant instances

    # Seed pizzas
    pizza1 = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
    pizza2 = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')

    db.session.add(pizza1)
    db.session.add(pizza2)
    db.session.commit()  # Commit the pizza instances

    # Seed restaurant_pizzas
    restaurant_pizza1 = RestaurantPizza(price=10, restaurant_id=restaurant1.id, pizza_id=pizza1.id)
    restaurant_pizza2 = RestaurantPizza(price=15, restaurant_id=restaurant1.id, pizza_id=pizza2.id)
    restaurant_pizza3 = RestaurantPizza(price=12, restaurant_id=restaurant2.id, pizza_id=pizza1.id)

    db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3])
    db.session.commit()  # Commit the restaurant_pizza instances