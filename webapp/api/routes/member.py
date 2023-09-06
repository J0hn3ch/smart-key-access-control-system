from http import HTTPStatus
from flask import Blueprint, render_template, abort
from flasgger import swag_from
from api.controller.member import MemberController
from api.schemas.member import MemberSchema

member_api = Blueprint('member_api', __name__)

# GET - Retrieve members
@member_api.route('/member')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': MemberSchema
        }
    }
})
def hello_member():
    """
    1 liner about the route
    A more detailed description of the endpoint
    --------
    """
    result = MemberModel()
    return MemberSchema().dump(result), 200

# POST - Creating new member
@member_api.route('/member', methods=['POST'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Member REST API for creating new member',
            'schema': MemberSchema
        }
    }
})
def create_member():
    """
    1 liner about the route
    A more detailed description of the endpoint
    --------
    """
    member = MemberModel()
    member.createMember('Melo')
    return MemberSchema().dump(member), 200

# UPDATE - Creating new member
@member_api.route('/member', methods=['UPDATE'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Member REST API for creating new member',
            'schema': MemberSchema
        }
    }
})
def update_member():
    """
    1 liner about the route
    A more detailed description of the endpoint
    --------
    """
    member = MemberModel()
    member.updateMember('Melo')
    return MemberSchema().dump(member), 200

# DELETE - Creating new member
@member_api.route('/member', methods=['DELETE'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Member REST API for creating new member',
            'schema': MemberSchema
        }
    }
})
def delete_member():
    """
    1 liner about the route
    A more detailed description of the endpoint
    --------
    """
    member = MemberModel()
    member.deleteMember('Melo')
    return MemberSchema().dump(member), 200