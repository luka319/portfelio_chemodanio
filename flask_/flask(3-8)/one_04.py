﻿from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return  render_template('index3.html')

app.run()

# !!! js не хочет
