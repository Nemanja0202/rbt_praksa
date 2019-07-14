from . import Config
import os

class Production(Config):

    ENV_TYPE = "Production" 

    DB_NAME = "d45su9ogur6ldl"
    DB_USER = "joyosfgmtisprr"
    DB_PASSWORD = "facae4452c2839f29908a13ef6063141606d3b7921c9d98f23dc6c1bfd866fd0"
    DB_HOST = "ec2-54-220-0-91.eu-west-1.compute.amazonaws.com"
    DB_PORT = 5432
    SQLALCHEMY_DATABASE_URI = "postgres://joyosfgmtisprr:facae4452c2839f29908a13ef6063141606d3b7921c9d98f23dc6c1bfd866fd0@ec2-54-220-0-91.eu-west-1.compute.amazonaws.com:5432/d45su9ogur6ldl"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    username = "Aleksa"
    password = "123456"
