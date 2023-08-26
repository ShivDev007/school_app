from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def Main():
    return render_template('index.html')
@app.route('/shivam')
def shivam():
    return "this is our shivam's Page"

if __name__=='__main__':
    app.run(debug=True)

