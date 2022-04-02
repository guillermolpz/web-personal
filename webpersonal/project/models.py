from webpersonal import db

class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    descripcion = db.Column(db.Text())
    
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        
    def __repr__(self):
        return f'Project: {self.titulo}'
