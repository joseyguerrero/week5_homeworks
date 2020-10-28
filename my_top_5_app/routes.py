from chicodes_blog_app import app

from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test')
def testRoute():
    top5s = ['My Hammock', 'My bed', 'My computer', 'My music', 'My cats']
    return render_template('test.html',list_names = top5s)