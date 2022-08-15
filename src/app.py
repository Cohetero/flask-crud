from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL
from flask import send_from_directory

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
import os

app = Flask(__name__)
engine = create_engine('mysql+pymysql://root:secret@localhost/personas')
Base = declarative_base()

class User(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer(), primary_key = True)
    name = Column(String(50), nullable = False)
    email = Column(String(50), nullable = False, unique = True)
    foto = Column(String(500), nullable = True)

    def __str__(self):
        return f"User (name={self.name}, email={self.email})"

Session = sessionmaker(engine)
session = Session()
# Conexión a la Base de Datos
#mysql = MySQL()
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'secret'
#app.config['MYSQL_DATABASE_DB'] = 'sistema'
#mysql.init_app(app)

CARPETA = os.path.join('uploads')
app.config['CARPETA'] = CARPETA

#Acceso a la carpeta Upload
@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(app.config['CARPETA'], nombreFoto)

# Creacion de las rutas
@app.route('/')
def index():
    users = session.query(User.id,
                        User.name,
                        User.email,
                        User.foto).all()
    return render_template('empleados/index.html', empleados = users)

@app.route('/destroy/<int:id>')
def destroy(id):
    session.query(User).filter(
        User.id == id
    ).delete()
    session.commit()
    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    user = session.query(User.id,
                        User.name,
                        User.email).filter(User.id == id).all()
    return render_template('empleados/edit.html', empleados = user)

@app.route('/update', methods=['POST'])
def update():
    _nombre = request.form['txtNombre']
    _correo = request.form['txtCorreo']
    _id = request.form['txtID']

    session.query(User).filter(
        User.id == _id
    ).update(
        {
            User.name: _nombre,
            User.email: _correo,
        }
    )
    session.commit()
    return redirect('/')

@app.route('/create')
def create():
    return render_template('empleados/create.html')

@app.route('/store', methods=['POST'])
def storage():
    _nombre = request.form['txtNombre']
    _correo = request.form['txtCorreo']
    _foto = request.files['txtFoto']

    if _nombre == '' or _correo == '':
        flash('Recuerda llenar los datos de los campos')
        return redirect(url_for('create'))

    user = User(name = _nombre, email = _correo)
    session.add(user)
    session.commit()
    return redirect('/')

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    user = User(name='Mauricio', email='mauricio@gmail.com')
    session.add(user)
    session.commit()
    app.run(host = "0.0.0.0",
            port = 4000,
            debug = True)
