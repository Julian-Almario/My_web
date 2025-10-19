from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portafolio')
def portafolio():
    return render_template('portafolio.html')

@app.route('/medcore')
def trabajos():
    return render_template('medcorework.html')

@app.route('/rddd')
def rddd():
    return render_template('rdddwork.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)