from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static/')
# !!! работает

@app.route('/')
@app.route('/index')
def index():
    return  render_template('index3.html')

app.run(debug=True)