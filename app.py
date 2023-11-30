import flask
from flask_restplus import Resource, Api

app = flask.Flask(__name__)
api = Api(app, '1.0', 'Api de conversão de temperatura', '')


def celsius_fahrenheit(temperatura=None):
    fahrenheit = (temperatura * 9 / 5) + 32
    return fahrenheit 

def fahrenheit_celsius(temperatura=None):
    celsius = (temperatura - 32) * 5 / 9
    return celsius

ns = api.namespace('temperatura', description='Conversões de temperatura.')

@ns.route('/celsius/<int:temperatura>fahrenheit')
class CelsiusFahrenheit(Resource):
    def get(self, temperatura):
        return celsius_fahrenheit(temperatura)

@ns.route('/fahrenheit/<int:temperatura>/celsius')
class FahrenheitCelsius(Resource):
    def get(self, temperatura):
        return fahrenheit_celsius(temperatura)

if __name__ == '__main__':
    app.run()
