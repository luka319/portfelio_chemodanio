from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return  render_template("""
            <script src = "{{ url_for('static', filename = 'my.js') }}">
            </script>

           <h1 style='color:green;'><u> Привет, мир, сиречь Hello world! </u> </h1>


    """)

app.run()