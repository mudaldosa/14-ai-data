from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "만나서 반갑습니다."

@app.route("/user/<userid>")
def profile(userid):
    return f"{userid}'s profile"

if __name__ == "__main__":
    app.run(debug=True)