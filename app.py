from flask import Flask
from flask_restful import Api

from sample_python_rest.hero import Hero

app = Flask(__name__)
api = Api(app)

api.add_resource(Hero, '/Hero/<string:get_name>')
app.run(debug=True)