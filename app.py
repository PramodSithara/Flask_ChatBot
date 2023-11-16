from flask import Flask, render_template, request, jsonify
import json
import googletrans
from googletrans import Translator # import google translate
translator = Translator()


app = Flask(__name__)

def load_responses():
    with open("responses.json", "r") as file:
        return json.load(file)

responses = load_responses()
default_response = "I'm sorry, I don't understand. Can you please rephrase your question?"
author = "Mr.Pramod.S.Jayansiri"


@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    return jsonify({"response": get_Chat_response(msg)})


def get_Chat_response(text):

    # Convert user input to lowercase for case-insensitive matching
    user_input = text.lower()

    # Check if the user input matches any predefined responses
    if user_input in responses:
        trans_answer = translator.translate(responses[user_input],dest='sinhala')
        return (trans_answer.text)
    elif user_input == "who create you" or user_input == "who make you":
        return author
    else:
        trans_default = translator.translate(default_response,dest='sinhala')
        return (trans_default.text)


if __name__ == "__main__":
    app.run()