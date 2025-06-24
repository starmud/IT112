# Import necessary libraries
# This is a simple Flask application that allows users to submit their names and stores them in a SQLite database.
# It also retrieves and displays all names stored in the database.
# The application uses Flask for the web framework and SQLite for the database.
# The HTML template is used to render the form and display the names.
from flask import Flask, request, render_template
import sqlite3

# Create a Flask application instance
# The Flask application is created using the Flask class
app = Flask(__name__)

# Initialize the SQLite database
# This function creates a SQLite database and a table to store names 
def init_db():
    # Connects to or creates a SQLite database file named 'data.db'
    with sqlite3.connect('data.db') as conn:
        # Create a table named 'entries' with two columns: id and name
        # the ID column is integer and is the primary key, while the name column is text
        conn.execute('CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY, name TEXT)')
        conn.commit() # Commit the changes to the database

# Define the main route of the application and allows both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def index(): # This function handles the main route of the application
    # If the request method is POST, it means the user has submitted a name
    if request.method == 'POST':
        # Get the name from the form data
        # The name is retrieved from the form data using request.form['name']
        name = request.form['name']
        
        # Inserts the submitted name into the database table 'entries'
        with sqlite3.connect('data.db') as conn:
            conn.execute('INSERT INTO entries (name) VALUES (?)', (name,))
            conn.commit() # Save the changes to the database
    
    # Retrieve all names from database 
    # This query selects all entries from the 'entries' table
    with sqlite3.connect('data.db') as conn:
        names = conn.execute('SELECT * FROM entries').fetchall()
    # Renders the index.html template with the list of names to display
    # The names are passed to the template as a variable named 'names'
    # The template will use this variable to display the names in a list
    # The render_template function is used to render the HTML template
    return render_template('index.html', names=names)

# Run the application
# This block checks if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    init_db() # ensure the database is initialized before running the app
    app.run(debug=True) # start the flask application in debug mode
# The debug mode allows for automatic reloading and provides a debugger in case of errors
# The application will be accessible at http://127.0.0.1:5000/