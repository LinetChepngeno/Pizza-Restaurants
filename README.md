## Flask Code Challenge - Pizza Restaurants
# Overview
This project involves building a Flask API for managing pizza restaurants. The API will handle CRUD operations for restaurants and pizzas, along with the ability to associate pizzas with restaurants and vice versa.

# Models
The following relationships need to be implemented:

1. A Restaurant has many Pizzas through RestaurantPizza
2. A Pizza has many Restaurants through RestaurantPizza
3. A RestaurantPizza belongs to a Restaurant and belongs to a Pizza

# Validations
Validations are required for the following models:

1. RestaurantPizza: Price must be between 1 and 30
2. Restaurant: Name must be less than 50 characters in length and must be unique

# Routes
The following routes need to be implemented:

# GET /restaurants

Returns a list of restaurants in the following JSON format:
json
Copy code
[
  {
    "id": 1,
    "name": "Dominion Pizza",
    "address": "Good Italian, Ngong Road, 5th Avenue"
  },
  {
    "id": 2,
    "name": "Pizza Hut",
    "address": "Westgate Mall, Mwanzi Road, Nrb 100"
  }
]
\
# GET /restaurants/:id

Returns details of a restaurant with associated pizzas if it exists. If not, returns an error message.
Successful response format:
json
Copy code
{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "Good Italian, Ngong Road, 5th Avenue",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}
Error response format:
json
Copy code
{
  "error": "Restaurant not found"
}

# DELETE /restaurants/:id

Deletes the restaurant with the specified ID along with associated RestaurantPizzas.
Successful response: Empty response body
Error response format:
json
Copy code
{
  "error": "Restaurant not found"
}
GET /pizzas

Returns a list of pizzas in the following JSON format:
json
Copy code
[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]
POST /restaurant_pizzas

Creates a new RestaurantPizza associated with an existing Pizza and Restaurant.
Request body format:
json
Copy code
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
Successful response format:
json
Copy code
{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}
Error response format:
json
Copy code
{
  "errors": ["validation errors"]
}

# Testing
To test the endpoints, you can use the following methods:

Run the Flask server and use tools like Postman to make requests.
Write unit tests using Flask's test client to programmatically test the endpoints.




