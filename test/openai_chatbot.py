from flask import Flask, request, jsonify
import openai
import datetime

app = Flask(__name__)
openai.api_key = "sk-123456789"  # Hardcoded key

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}],
    )
    return jsonify({"response": response["choices"][0]["message"]["content"]})
