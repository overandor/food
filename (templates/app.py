from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sms", methods=["POST"])
def receive_sms():
    from_number = request.form.get("From")
    message = request.form.get("Body")
    print(f"📩 Received SMS from {from_number}: {message}")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
