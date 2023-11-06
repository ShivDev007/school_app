# from flask import Flask, render_template

# app = Flask(__name__)
# @app.route("/")
# def main():
#     return render_template('index.html')
# @app.route('/shivam')
# def shivam():
#     return "this is our shivam's Page"

# if __name__=='__main__':
#     app.run(debug=True, host="0.0.0.0")



# Import the Flask and MySQL Connector modules
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

# Create a Flask app object
app = Flask(__name__)

# Create a MySQL database connection object
db = mysql.connector.connect(
    host="65.0.183.157",
    user="root",
    password="root",
    database="blog"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Define the route for the home page
@app.route("/")
def index():
    # Fetch all the blog posts from the database
    cursor.execute("SELECT * FROM blog_posts")
    posts = cursor.fetchall()
    # Render the index.html template and pass the posts as a parameter
    return render_template("index.html", posts=posts)

# Define the route for the admin page
@app.route("/admin")
def admin():
    # Render the admin.html template
    return render_template("admin.html")

# Define the route for adding a new blog post
@app.route("/add", methods=["POST"])
def add():
    # Get the title and image URL from the form data
    title = request.form.get("title")
    image = request.form.get("image")
    # Insert the new blog post into the database
    cursor.execute("INSERT INTO blog_posts (title, image) VALUES (%s, %s)", (title, image))
    db.commit()
    # Redirect to the home page
    return redirect(url_for("admin"))

# Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)


