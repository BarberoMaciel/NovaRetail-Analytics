from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "project": "Nova Retail Analytics",
        "status": "API running"
    }

if __name__ == "__main__":
    app.run(debug=True)