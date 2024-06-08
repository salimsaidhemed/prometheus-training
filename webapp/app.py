from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Gauge,Counter
import random
import time

app = Flask(__name__)
metrics = PrometheusMetrics(app)
REQUESTS = Counter("requests_total","Total Number of Requests Made")
SALES = Counter("sale","Total Sale for Product",["product","price"])
PRODUCTS = [
    {"name": "T-shirts", "price": 30},
    {"name": "Polo shirts", "price": 50},
    {"name": "Dress shirts", "price": 100},
    {"name": "Blouses", "price": 80},
    {"name": "Jeans", "price": 100},
    {"name": "Pants", "price": 80},
    {"name": "Shorts", "price": 50},
    {"name": "Skirts", "price": 80},
    {"name": "Dresses", "price": 150},
    {"name": "Blazers", "price": 200},
    {"name": "Jackets", "price": 300},
    {"name": "Sweaters", "price": 100},
    {"name": "Hoodies", "price": 80},
    {"name": "Sweatshirts", "price": 80},
    {"name": "Coats", "price": 300},
    {"name": "Suits", "price": 500},
    {"name": "Activewear", "price": 100},
    {"name": "Sleepwear", "price": 50},
    {"name": "Undergarments", "price": 50},
    {"name": "Socks", "price": 20},
    {"name": "Scarves", "price": 50},
    {"name": "Hats", "price": 50},
    {"name": "Gloves", "price": 50},
    {"name": "Belts", "price": 50},
    {"name": "Handbags", "price": 200},
    {"name": "Backpacks", "price": 150},
    {"name": "Wallets", "price": 100},
    {"name": "Shoes", "price": 200},
    {"name": "Accessories", "price": 100},
    {"name": "Swimwear", "price": 100}
]


def sale_product():
    product_index = random.randint(0,len(PRODUCTS)-1)
    price = PRODUCTS[product_index]["price"]
    SALES.labels(PRODUCTS[product_index]["name"],price).inc()




@app.route("/shop")
def shop():
    sale_product()
    return "Thanks for Shopping with Us"

if __name__ == '__main__':
    app.run()
