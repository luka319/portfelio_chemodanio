from flask import Flask, render_template

#app = Flask(__name__, static_url_path='/static')
app = Flask(__name__)
# !!! работает

@app.route('/')
def index():
    return  render_template('index3.html')


@app.route('/kartinka/')
@app.route('/kartinka')
def dictionary8():
    #name = 'Александр'
    #num01 = 2018


    return  render_template('index8_картинка.html')


app.run(debug=True)