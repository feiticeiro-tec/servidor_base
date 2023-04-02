"""NAMESPACE USUARIO"""
from flask_restx import Resource
from flask_restx._http import HTTPStatus
from server.api.form.usuario import form_criacao
from server.api.serializer.usuario import serializer_usuario
from server.api import api

np_usuario = api.namespace('usuario', 'Rotas relacionadas ao usuario logado!')


@np_usuario.route('/', methods=['POST', 'GET'])
@np_usuario.route('/<uuid:uuid>', methods=['GET', 'DELETE', 'PATCH'])
class Usuario(Resource):
    """VIEW DE CONTROLE DE USUARIO"""

    @np_usuario.expect(form_criacao)
    @np_usuario.marshal_with(serializer_usuario,
                             code=HTTPStatus.CREATED,
                             description='Usuario Criado Com Sucesso!')
    def post(self):
        """Criação"""
        return

    def get(self, uuid: str = None):
        """Detalhamento"""
        return uuid

    def delete(self, uuid: str):
        """Desativação"""
        return uuid

    def patch(self, uuid: str):
        """Atualização"""
        return uuid


@np_usuario.route('/auth')
class Auth(Resource):
    """View de authenticação"""

    def post(self):
        """Login"""
        return
