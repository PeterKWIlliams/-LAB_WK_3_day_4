from app import app
from flask import render_template
from models import order 
from models.customer import customers


@app.route('/order')
def index():
    return render_template("index.html",title ="Home",customers = customers)

@app.route('/order/<int:index_order>')
def index(index_order):
  index_order -= 1
  return render_template("order.html", order_num = index_order + 1, order_1 = customers[index_order])

