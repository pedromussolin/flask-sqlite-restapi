from flask import Blueprint, jsonify, request, abort
from .models import User
from . import db


main = Blueprint('main', __name__)


# GET ALL USERS - GET
@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': u.id, 'nome': u.nome, 'email': u.email, 'celular': u.celular} for u in users])


# GET USER BY ID - GET
@main.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404)
    return jsonify({'id': user.id, 'nome': user.nome, 'email': user.email, 'celular': user.celular})


# CREATE USER - POST
@main.route('/users', methods=['POST'])
def create_user():
    if not request.json or not 'nome' in request.json or not 'email' in request.json:
        abort(400)
    new_user = User(
        nome=request.json['nome'],
        email=request.json['email'],
        celular=request.json.get('celular', '')
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id, 'nome': new_user.nome, 'email': new_user.email, 'celular': new_user.celular}), 201


# EDIT USER - PUT
@main.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404)
    if not request.json:
        abort(400)
    user.nome = request.json.get('nome', user.nome)
    user.email = request.json.get('email', user.email)
    user.celular = request.json.get('celular', user.celular)
    db.session.commit()
    return jsonify({'id': user.id, 'nome': user.nome, 'email': user.email, 'celular': user.celular})


# DELETE USER - DELETE
@main.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'result': True})
