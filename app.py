from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/",  methods=['POST', 'GET'])
def home():
    ##return("Teste")
    return render_template("index.html")

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)