from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def hello_worl():
    names="harry"
    return render_template('index2.html',name=names)

@app.route('/boot')
def hello():
    return render_template('boot.html')

if __name__ == '__main__':
    app.run(debug=True)