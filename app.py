from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models
from models import Restaurant, Pizza, RestaurantPizza

# Routes
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    result = [{'id': r.id, 'name': r.name, 'address': r.address} for r in restaurants]
    return jsonify(result)

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        pizzas = [{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in restaurant.pizzas]
        result = {'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address, 'pizzas': pizzas}
        return jsonify(result)
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        for rp in restaurant.pizzas:
            db.session.delete(rp)
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    result = [{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in pizzas]
    return jsonify(result)

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    pizza = Pizza.query.get(data.get('pizza_id'))
    restaurant = Restaurant.query.get(data.get('restaurant_id'))
    if pizza and restaurant:
        rp = RestaurantPizza(price=data.get('price'), pizza=pizza, restaurant=restaurant)
        db.session.add(rp)
        try:
            db.session.commit()
            return jsonify({'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients})
        except:
            return jsonify({'errors': ['validation errors']}), 400
    else:
        return jsonify({'errors': ['Pizza or Restaurant not found']}), 404

if __name__ == '__main__':
    app.run(debug=True)