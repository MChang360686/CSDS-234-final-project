# CSDS-234-final-project
Final Project for CSDS 234 Structured and Unstructured Data

Sample data to populate the database has been provided in the folder data-used.  The actual csv files that were used could not be published to the Git because of their size.

Problem 1 is solved by creating a web application that can accept queries on the data given

Problem 2 is handled by the queries provided for each subproblem within the final report.
1. 
    1. SELECT Title FROM product WHERE asin = {similar product 1} OR asin =
{similar product 2} OR asin = {similar product 3} OR asin = {similar product
4} OR asin = {similar product 5};
    2. SELECT customer FROM reviews, product WHERE reviews.asinindex =
product.index AND product.asin = {selected similar product};

2. 
    1. SELECT asin FROM product WHERE salesrank > {threshold number};
    2. SELECT Title FROM product WHERE asin = {similar product 1} OR asin =
{similar product 2} OR asin = {similar product 3} OR asin = {similar product
4} OR asin = {similar product 5};

3.
    1. SELECT Title, asin FROM product, categories WHERE
sci="Books[283155]" AND scii = "Subjects[1000]" AND sciii = "Religion &
Spirituality[22]" GROUP BY Title;

# Use Instructions
1. Ensure MySQL is running
2. Using MySQL Workbench, import model with csds234finalproject.mwb and forward engineer the database
3. Populate database with either sample data from data-used OR strip the data using data-analytics-engine.py, Reviews.py, and categories.py
4. Run app.py

# Files
- app.py
  - Contains queries and Flask app routes.  Running this file will host the web application at 127.0.0.1:5000
- data-analytics-engine.py
  - Strips products and related information from text file into dataframe and converts dataframe into csv file
- categories.py
  - Strips category information into dataframe and converts it into a csv file
- Reviews.py
  - Strips the review information into a dataframe and converts it into a csv file
- HowManyCategories.py
  - Counts the number of subcategories within a product's category
- HowManyReviews.py
  - Counts the greatest number of reviews products can have
- csds234finalproject.mwb
  - Model file to forward engineer the database

# Directories
- templates
   - Contains the HTML files needed to display information
- data-used
  - Originally supposed to contain the csv files containing the data used in the project, GitHub's 25mb file size limit hindered this, and as a result there are only sample files that can be imported into the database
