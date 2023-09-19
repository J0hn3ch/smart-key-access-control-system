from http import HTTPStatus
from flask import Blueprint, render_template, abort
from flasgger import swag_from
from api.schemas.welcome import WelcomeSchema

home_api = Blueprint('api', __name__)

@home_api.route('/')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': WelcomeSchema
        }
    }
})

def welcome():
    """
    1 liner about the route
    A more detailed description of the endpoint
    --------
    """
    result = "Hello World!"
    return result