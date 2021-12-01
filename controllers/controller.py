from app import app
from flask import render_template
from models import order 
from models.customer import customers


@app.route('/order')
def index():
    return render_template("index.html",title ="Home",customers = customers  )

