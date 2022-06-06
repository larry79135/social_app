from flask import Flask,render_template,jsonify

from mysql import query
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# query=[ 
#         {
#         "id": 2,
#         "city_name": "London",
#         "country_name": "United Kingdom",
#         "is_capital": True,
#         "location": {
#             "longitude": -0.114089,
#             "latitude": 51.507497
#             }
#         }
#     ]
       
@app.route("/")
def hello():
    return "Hello, World!"
@app.route("/home")
def home():
    
    return jsonify(query(request.args.get('type')))









if __name__ == '__main__':
    app.run()