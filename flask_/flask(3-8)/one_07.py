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


@app.route('/index4/big/b/i/g/')
def index4big():
    name = 'Александр Big'
    num01 = 2000181818
    return  render_template('index4.html', name=name, num01=num01)


def index5def():
    name = 'Александр2'
    num01 = 20182
    return  render_template('index4.html', name=name, num01=num01)

app.add_url_rule('/index5/', 'i5', index5def)


def index5big():
    name = 'Александр5 Big'
    num01 = 2018256789
    return  render_template('index4.html', name=name, num01=num01)

app.add_url_rule('/index5/big/b/i/g/', 'i5big', index5big)



app.run(debug=True)