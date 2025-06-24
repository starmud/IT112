from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///names.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Simple Name Model
class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    names = Name.query.all()
    return render_template('index.html', names=names)

@app.route('/add_name', methods=['POST'])
def add_name():
    name = request.form.get('name')
    
    # Simple validation - check if name is filled
    if name and name.strip():
        new_name = Name(name=name.strip())
        db.session.add(new_name)
        db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)