import flask
from flask import request, jsonify
from flask_restplus import Resource, Api

app = flask.Flask(__name__)
api = Api(app)

def celsius_fahrenheit(temperatura=None):
    fahrenheit = (temperatura * 9 / 5) + 32
    return fahrenheit 

def fahrenheit_celsius(temperatura=None):
    celsius = (temperatura - 32) * 5 / 9
    return celsius

@api.route('/', methods=['GET'])
def home():
    return "Api de Conversão em Python-v3"

@api.route('/celsius/<int:temperatura>fahrenheit')
class CelsiusFahrenheit(Resource):
    def get(self, temperatura):
        return jsonify(celsius_fahrenheit(temperatura))

@api.route('/fahrenheit/<int:temperatura>/celsius')
class FahrenheitCelsius(Resource):
    def get(self, temperatura):
        return jsonify(fahrenheit_celsius(temperatura))


if __name__ == '__main__':
    app.run()
