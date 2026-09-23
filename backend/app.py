from flask import Flask, jsonify, request, render_template
from battery import Battery

app = Flask(__name__, static_folder="static", template_folder="templates")
battery = Battery()

# Serve frontend
@app.route("/")
def index():
    return render_template("index.html")

# API endpoints
@app.route("/status", methods=["GET"])
def status():
    return jsonify(battery.status())

@app.route("/charge", methods=["POST"])
def charge():
    amount = request.json.get("amount", 10)
    return jsonify({"level": battery.charge(amount)})

@app.route("/discharge", methods=["POST"])
def discharge():
    amount = request.json.get("amount", 10)
    return jsonify({"level": battery.discharge(amount)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
