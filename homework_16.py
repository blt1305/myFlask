from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/')
# def hello_world():
#     return '<p>Hello, World!</p>'

@app.route('/again')
def again():
    return '<h1>I am glad to see you.</h1>'

if __name__ == '__main__':
    app.run(debug=True)









