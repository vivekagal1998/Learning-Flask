from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    names = {'name1': name, 'age': 18, 'clg': 'SVNIT'}
    itemss = [{'Hack': 'Vivek', 'age': 18, 'job': 'Problem Setter'}, {'don': 'random', 'dsk': 'edvkf'}]

    comments = ['vivek', 1, 2, 3]

    return render_template('user.html', names = names, name = name, val = 'False', itemss = itemss, comments = comments)

if __name__ == '__main__':
    app.run(debug = True)
