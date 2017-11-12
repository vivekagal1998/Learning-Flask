from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    num = [1, 2, 3, 4, 5]
    return render_template('index_macro.html', name = 'Vivek', num = num)

if __name__ == '__main__':
    app.run(debug = True)
