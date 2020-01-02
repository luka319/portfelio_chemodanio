from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static/')
# !!! работает

@app.route('/')
@app.route('/index')
def index():
    return  render_template('index3.html')


@app.route('/index4')
def index4():
    name = 'Александр'
    num01 = 2018
    return  render_template('index4.html', name=name, num01=num01)


app.run(debug=True)