"""FORMULARIOS RELACIONADO AO USUARIO"""
from flask_restx.reqparse import RequestParser
from server.api.form.form_types import string


form_criacao = RequestParser()
form_criacao.add_argument('username', type=string,
                          required=True, location='form')
form_criacao.add_argument('password', type=string,
                          required=True, location='form')
