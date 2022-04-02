from flask import render_template, Blueprint, request, redirect, url_for

from webpersonal import project
#from webpersonal.project.models import PROJECTS
from webpersonal.project.models import Project
from webpersonal import db


project = Blueprint('project', __name__)

@project.route('/project')
def projects():
    projects = Project.query.all()
    db.session.commit()
    return render_template('project/projects.html', projects=projects)

@project.route('/project/crear')
def crear():
    return render_template('project/crear.html')

@project.route('/project/insert', methods=['POST'])
def insert():
    #titulo = request.form['titulo']
    titulo = request.form.get('titulo')
    descripcion = request.form.get('descripcion')
    
    project = Project(titulo, descripcion)
    db.session.add(project)
    db.session.commit()
    
    return redirect(url_for('project.projects'))

@project.route('/project/editar/<int:id>')
def editar(id):
    project = Project.query.get_or_404(id)
    
    return render_template('project/editar.html', project=project)

@project.route('/project/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    #titulo = request.form['titulo']
    project = Project.query.get_or_404(id)
    project.titulo = request.form.get('titulo')
    project.descripcion = request.form.get('descripcion')
    
    db.session.add(project)
    db.session.commit()
    
    return redirect(url_for('project.projects'))

@project.route('/project/eliminar/<int:id>')
def eliminar(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    
    return redirect(url_for('project.projects'))