import flask
from flask import Flask, request, render_template, Response
from flask_cors import CORS
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

from main_logic import service
import pandas as pd

app = flask.Flask(__name__)
CORS(app)


@app.route("/rank", methods=['POST'])
def predict():
    # initialize the data dictionary that will be returned from the
    # view
    data = {"success": False}
    input_json = request.json

    try:
        df = service(input_json)
        return Response(df.to_json(orient="records"), mimetype='application/json')
    except Exception as exc:
        print("exception")
        data["prediction_Exception"] = str(exc)
        return data
    

# if this is the main thread of execution first load the model and
@app.route("/")
def homepage():
    return "Hey Welcome to Rank Predictor!"


if __name__ == "__main__":
    app.run()