from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from SpendSmart"

@app.route("/about")
def about():
    return "SpendSmart is a practice WebApp to track finance"

if __name__ == "__main__":
    app.run(debug=True)

