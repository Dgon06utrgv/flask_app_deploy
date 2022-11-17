from flask import Flask, render_template





app = Flask(__name__)
@app.route("/")
def main2():
  return render_template("portfolio example.html")

@app.route("/example")
def hello_world2():
    return render_template('base.html')
  
@app.route("/<path:filepath>")  
def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

app.run(host='0.0.0.0',port=8080,debug=False)