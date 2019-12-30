from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import util_functions as utils

app = Flask(__name__)
api = Api(app)

class Double_Side_Prime(Resource):
    def get(self, number):
        result = utils.is_double_side_prime(number)
        resultStr = "{} is not a double side prime number"
        if(result):
            resultStr = "{} is a double side prime number"        
        return jsonify(resultStr.format(number))
  

api.add_resource(Double_Side_Prime, '/doubleprime/<number>')


if __name__ == '__main__':
     app.run()
  


    



