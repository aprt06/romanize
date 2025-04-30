from flask import Flask, request, jsonify, render_template
from pythainlp.transliterate import romanize
import os
app = Flask(__name__)
print(1)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    try:
        data = request.get_json()
        if not data or "text" not in data:
            return jsonify({"error": "Missing 'text'"}), 400

        romanized = romanize(data["text"],engine="thai2rom")
        return jsonify({"romanized": romanized})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
   app.run()