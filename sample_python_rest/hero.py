from flask_restful import Resource

from sample_python_rest.data import names


class Hero(Resource):

    def get(self, get_name):
        for name in names:
            if (get_name == name["name"]):
                return name['name'], 200
        return '{} not found'.format(get_name), 401