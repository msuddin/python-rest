from flask_restful import Resource

from sample_python_rest.data import names


class Hero(Resource):

    def get(self, get_name):

        for name in names:
            if (get_name == name['name']):
                return name['name'], 200

        return '{} not found'.format(get_name), 401

    def post(self, get_name):

        for name in names:
            if (get_name == name['name']):
                return 'Unable to add {} as it already exists'.format(name['name']), 401

        new_name = {"name": get_name}
        names.append(new_name)

        return '{} has been added'.format(get_name), 201