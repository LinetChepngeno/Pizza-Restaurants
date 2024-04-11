from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    address = db.Column(db.String(120), nullable=False)
    pizzas = db.relationship('Pizza', secondary="restaurant_pizzas", backref='restaurants')

class Pizza(db.Model):
    __tablename__ = "pizzas"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)

class RestaurantPizza(db.Model):
    __tablename__ = "restaurant_pizzas"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False) 
    restaurant_id=db.Column( db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id=db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    

    __table_args__ = (
        db.CheckConstraint('price >= 1 AND price <= 30', name='price_range'),
    )