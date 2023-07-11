from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key= "sneaky"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def display():
    return render_template("display.html")

if __name__=="__main__":
    app.run(debug=True, port=5050)