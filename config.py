from decouple import config

class Config:
    SECRET_KEY = 'JJHkg23!54K*SJNDK_Aaa"'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '12345678'
    MYSQL_DB = 'tienda1'
    MAIL_SERVER= 'smtp.googlemail.com'
    MAIL_PORT = 587 #TLS:Transport Layer Security:Seguridad de la capa de transporte
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'emailAdmin@gmail.com'
    MAIL_PASSWORD = config('MAIL_PASSWORD')

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
