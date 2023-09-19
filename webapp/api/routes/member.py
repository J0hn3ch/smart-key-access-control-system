from http import HTTPStatus
from flask import Blueprint, render_template, abort, request, make_response
from flasgger import swag_from
from api.controllers.member import MemberController
from api.schemas.member import MemberSchema
from api.models.member import Member

import os

member_api = Blueprint('member_api', __name__)

# GET - Retrieve members
@member_api.route('/member', methods=['GET','POST'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': MemberSchema
        }
    }
})
def manage_member():
    """
    1 liner about the route
    A more detailed description of the endpoint
    --------
    """

    memberController = MemberController()
    student_id = request.args.get('student_id')
    if student_id is not None:
        members = [ memberController.getMemberById(student_id) ]
        if len(members) > 0:
            return render_template('member.html', members=members)
    else:
        members = memberController.getAllMembers()
        return render_template('member.html', members=members)
        #response = MemberSchema().dump(memberController), 200
        #return response
    
    #template = os.getcwd() + "/templates" + "/member.html"
    
    

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
    member = MemberController()
    member.createMember('Melo')
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
        try:
            searchword = request.args.get('key', '')
        except KeyError:
            tb = sys.exception().__traceback__
            raise OtherException(...).with_traceback(tb)
        resp = make_response("Record not found", 400)
        resp.headers['X-Something'] = 'A value'
    return render_template('login.html', error=error)

    #return MemberSchema().dump(member), 200

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
    memberController = MemberController()

    student_id = request.args.get('student_id')
    if student_id is not None:
        memberController.deleteMember(student_id)
        response = MemberSchema().dump(memberController), 200
    else:
        response = "Select member to delete"

    return response