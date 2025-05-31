from flask import Flask
# This is a simple Flask application with two routes: home and reporter.
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
   return '<h1>Hello, World!</h1>'

@app.route('/reporter')  #This route is for the reporter page
@app.route('/reporter/<int:reporter_id>') #converts reporter_id to an integer, converter: 'int', converter: variable: 'reporter_id'
def reporter(reporter_id=None): # This function handles the reporter page
  # You can add logic here to fetch reporter details or any other data
  # For now, we will just return a simple string
    if reporter_id is None:
        return "<h2>No reporter ID provided.</h2><a href='/'>Return to home page</a>"
    # python f-string for formatting
    return f''' 
    <h2>Reporter #{reporter_id} Bio</h2>
    <a href="/">Return to home page</a>
    '''

@app.route('/article')
@app.route('/article/<article_name>')
def article(article_name=None):
    if article_name is None:
      return "<h2>No article name provided.</h2><a href='/'>Return back to home page</a>"
    
    return f'''
    <h2>{article_name.replace('-', ' ').title()}</h2> 
    <a href="/">Return back to home page</a>
    ''' # This function handles the article page, replacing hyphens with spaces and capitalizing words, x.com/article/article-name