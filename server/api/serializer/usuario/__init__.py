"""SERIALIZERS DA ROTA USUARIO"""
from flask_restx import fields
from server.api import api


serializer_usuario = api.model("Usuario", {
    "username": fields.String
})
