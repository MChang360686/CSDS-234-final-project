#!/usr/bin/python3


from flask import Flask, request, render_template, url_for, flash, redirect
from dotenv import load_dotenv
import os
#import requests
#from requests.exceptions import ConnectionError
import mysql.connector
from mysql.connector import Error

# Create a connection
class DatabaseConnectionCredentials(object):
    def __init__(self, host, username, password, database, port):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port


load_dotenv(override=True)

dbCredentials = DatabaseConnectionCredentials(
    host=os.getenv("HOST"),
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("DATABASE"),
    port=os.getenv("PORT"))

# Check .env values here
# print(vars(dbconnCredentials))

# Method to setup connection
def __acquire_dbconnection():
    try:
        db = mysql.connector.connect(
            host=dbCredentials.host,
            user=dbCredentials.username,
            passwd=dbCredentials.password,
            database=dbCredentials.database,
            port=dbCredentials.port)
    except mysql.connector.Error as e:
        print(f"Error {e}")
    return db

# Queries

# Get all products
def queryProducts():
    db = __acquire_dbconnection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM mydb.product")
    result = cursor.fetchall()
    db.close()
    return result

# Sample query
def sampleQuery():
    db = __acquire_dbconnection()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM product, categories WHERE categories.asinindex = product.index AND categories.sci="Books[283155]" LIMIT 10;')
    result = cursor.fetchall()
    db.close()
    return result

# Find customers who bought books
def bookQuery():
    db = __acquire_dbconnection()
    cursor = db.cursor()
    cursor.execute('SELECT customer FROM product, categories, reviews WHERE product.index = categories.asinindex AND categories.sci= "Books[283155]" GROUP BY customer;')
    result = cursor.fetchall()
    db.close()
    return result

# Find customers who purchased religious books
def bookReligiousQuery():
    db = __acquire_dbconnection()
    cursor = db.cursor()
    cursor.execute('SELECT customer FROM product, categories, reviews WHERE product.index = categories.asinindex AND categories.sci = "Books[283155]" AND categories.scii = "Subjects[1000]" AND categories.sciii = "Religion & Spirituality[22]" GROUP BY customer;')
    result = cursor.fetchall()
    db.close()
    return result


# I decided it would be more convenient to run
# a query rather than make a method for each query
# Probably unsafe from a best practices view, but that's OK for this project
def runquery(sql):
    db = __acquire_dbconnection()
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return result


# Create flask webapp and configure
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Index/Landing page
@app.route('/')
def index():
    return render_template("index.html")

# Page that displays the results of a sample query
@app.route('/samplequery')
def samplequery():
    queryResult = sampleQuery()
    return render_template("samplequery.html", data=queryResult)

# Page that displays all of the products in the database
@app.route('/allproducts')
def queryAllProducts():
    queryResult = queryProducts()
    return render_template("allproducts.html", data=queryResult)

# Who purchased books
@app.route('/bookpurchase')
def showpeoplewhoboughtbooks():
    queryResult = bookQuery()
    return render_template('bookcustomers.html', data=queryResult)

# WHo purchased religious books
@app.route('/religiousbookpurchase')
def showpeoplewhoboughtreligiousbooks():
    queryResult = bookReligiousQuery()
    return render_template('bookcustomersreligious.html', data=queryResult)


# Create search for related products route
@app.route('/searchforproducts', methods=["POST", "GET"])
def searchforproducts():
    if request.method == "POST":
        query = request.form["query"]
        return redirect(url_for("enteredQuery", querystring=query))
    else:
        return render_template('searchforproducts.html')

# The redirect for searchforproducts
@app.route('/<querystring>')
def enteredQuery(querystring):
    qu = runquery(querystring)
    return render_template('resultlandingpage.html', data=qu)


# Create search for customers who bought similar products route
@app.route('/similarcategories', methods=["POST", "GET"])
def similarcategories():
    if request.method == "POST":
        query = request.form["catquery"]
        return redirect(url_for('findsimilarcategories', querycategories=query))
    else:
        return render_template('similarcategories.html')

# redirect from /similarcategories
@app.route('/<querycategories>')
def findsimilarcategories(querycategories):
    que = runquery(querycategories)
    return render_template('categoryresultpage.html', categorydata=que)


# Create search for Reviews
@app.route('/reviews', methods=["POST", "GET"])
def queryreviews():
    if request.method == "POST":
        query = request.form["reviewquery"]
        return redirect(url_for('findreviews', queryreviews=query))
    else:
        return render_template('findreview.html')

# Redirect from /reviews
@app.route('/<queryreviews>')
def findreviews(queryreviews):
    q = runquery(queryreviews)
    return render_template('reviewresults.html', data=q)


# Create search for Customers
@app.route('/customersearch', methods=["POST", "GET"])
def findcustomer():
    if request.method == "POST":
        query = request.form["customerquery"]
        return redirect(url_for('getcustomers', customers=query))
    else:
        return render_template('findcustomers.html')

# Redirect from /customersearch
@app.route('/<customers>')
def getcustomers(customers):
    q = runquery(customers)
    return render_template('customerqueryresults.html', data=q)



# Main method to run app
if __name__ == '__main__':
    app.run(debug=True)