from flask import Flask, render_template, request, Response
from core import get_product_list
from flask_cors import CORS
import json

app = Flask(__name__)

# Enable CORS
# Cross-origin resource sharing is a mechanism that allows restricted resources
# on a web page to be requested from another domain outside the domain from
# which the first resource was served
CORS(app=app)

# 1. Rendering simple html
# 2. Note: Method is an optional parameter
@app.route("/", methods=["GET"])
def welcome():
    return render_template("index.html")

# 1. Taking parameters from path (Note: type ensuring is optional)
# 2. Using Jinja to render htmls with dynamic input (literals and statements)
# 3. Accessing methods from other files
@app.route("/users/<string:username>", methods=["GET"])
def welcome_user(username):
    product_list = get_product_list()
    return render_template("user.html", user=username, random_dict=product_list)

# 1. Taking the data from the request
# 2. Returning a Http Response with JSON data
@app.route("/product", methods=["GET", "POST"])
def get_products():
    input_json = request.json
    product_list = get_product_list()
    try:
        product_name = input_json['product_name']
        data = {"product_name": product_name, "price": product_list[product_name], "metadata": {"status": "success"}}
        return Response(json.dumps(data), status=200,  mimetype='application/json')
    except:
        data = {"product_name": product_name, "metadata": {"status": "fail", "error": "Product doesn't exist"}}
        return Response(json.dumps(data), status=404,  mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
