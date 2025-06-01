# main class; entry point for the flask application
# render template uses the set template for each html page
from flask import Flask, render_template

# creats the application instance, name (main) is used to locate resources
app = Flask(__name__)

# Define routes for the application
# routing is used to map URLs to functions

# homepage route
@app.route('/') #default route website.com/
def home():
    # renders home.html (pulls template from templates folder)
    # render_template is a Flask function that renders an HTML template
    return render_template('home.html')

# about page route
@app.route('/about') # website.com/about
def about():
    # renders about.html (template from templates folder)
    # this function is called when the user visits the /about URL
    # render_template is a Flask function that renders an HTML template
    return render_template('about.html')

# contact page route
@app.route('/contact') # website.com/contact
def contact():
    # renders contact.html (template from templates folder)
    # this function is called when the user visits the /contact URL
    # render_template is a Flask function that renders an HTML template
    return render_template('contact.html')

# runs the application if this file is run directly (not pulled or imported)
if __name__ == '__main__':
    # run the application with debug mode enabled
    app.run(debug=True)
