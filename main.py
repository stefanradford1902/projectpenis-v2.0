import mysql.connector
from flask import Flask, request, render_template
app = Flask(__name__, static_url_path='')

mydb = mysql.connector.connect(
  host="localhost",
  user="Prototype",
  passwd="sdr170901",
  database="stms"
)

print(mydb)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/profit-stats')
def profit_stats():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM stats")
    result = str(cursor.fetchall())
    return result

@app.route('/items-to-be-reordered')
def items_to_be_reordered():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM items_to_be_reordered")
    result = str(cursor.fetchall())
    return result

@app.route('/items-to-be-shipped')
def items_to_be_shipped():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM items_to_be_shipped")
    result = str(cursor.fetchall())
    return result

@app.route('/items-to-be-sold', methods = ['GET', 'POST'])
def items_to_be_sold():
  if request.method == 'GET':
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM items_to_be_sold")
    result = str(cursor.fetchall())
    return render_template('items-to-be-sold.html')
  elif request.method == 'POST':
    items = str(request.form.get('item'))
    quantity = str(request.form.get('quantity'))
    buyingPrice = str(request.form.get('buyingprice'))
    estimatedSellPrice = str(request.form.get('estimatedsellprice'))
    bought = str(request.form.get('bought'))
    data = [items, quantity, buyingPrice, estimatedSellPrice, bought]
    return str(data)
  else:
    return "invalid method", 405


@app.route('/edit/<pagesold>')
def edit_pagesold(pagesold):
  page = str(pagesold)
  if pagesold == "items-to-be-sold":
    return render_template('items-to-be-sold-edit.html')
  else:
    return "404", 404

@app.route('/edit/<pageshipped>')
def edit_pageshipped(pageshipped):
  pageshipped = str(page1)
  if pageshipped == "items-to-be-shipped":
    return render_template('items-to-be-shipped-edit.html')
  else:
    return "404", 404

@app.route('/edit/<pagereordered>')
def edit_pagereordered(pagereordered):
  pagereordered = str(pagereordered)
  if pagereordered == "items-to-be-reordered":
    return render_template('items-to-be-reordered-edit.html')
  else:
    return "404", 404


app.run(host='127.0.0.1', port=3000)