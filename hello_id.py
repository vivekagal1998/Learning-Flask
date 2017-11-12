from flask import Flask
app = Flask(__name__)

@app.route('/user/<int:name>')
def user(name):
    return "<h1>Hello, %s </h1>" % name

if __name__ == '__main__':
    app.run(debug = True)
