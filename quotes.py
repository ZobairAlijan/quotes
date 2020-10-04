from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:1370937@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://uyaeaglseoldtu:84d81ad85af7ef4d403404fc972ca57f408c121f7acc2da1231edd690afba202@ec2-34-235-62-201.compute-1.amazonaws.com:5432/dfih1u0tlfic8p'
app.config['SQLALECHMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))
    
    
@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html', result=result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    
    quotedata = Favquotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))



app.run(port=5000)