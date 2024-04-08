from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

restaurant_pizza = db.Table('restaurant_pizza',
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id'), primary_key=True),
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.id'), primary_key=True),
    db.Column('price', db.Integer, nullable=False)
)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    address = db.Column(db.String(120), nullable=False)
    pizzas = db.relationship('Pizza', secondary=restaurant_pizza, backref='restaurants')

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)

class RestaurantPizza(db.Model):
    __table__ = restaurant_pizza
    __table_args__ = (
        db.CheckConstraint('price >= 1 AND price <= 30', name='price_range'),
    )