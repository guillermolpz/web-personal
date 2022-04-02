from distutils.debug import DEBUG


class Config:
    #Configuracion base
    DEBUG = True
    TESTING = True
    
    #Configuración de Base de Datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql01@localhost:3306/webpersonal"
    
class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True