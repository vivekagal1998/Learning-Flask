from flask import Flask

app = Flask(__name__)

req = ''

@app.after_request
def after_request(resp):
    global req
    req += ' after '
    return resp

@app.teardown_request
def tear_request(excep):
    global req
    req += ' tear<br> '
    return req

@app.route('/')
def index():
    return 'Hello ' + req

@app.before_request
def before_request():
    global req
    req += 'before '


if __name__ == '__main__':
    app.run(debug = True)
