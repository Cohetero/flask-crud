from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL
from flask import send_from_directory
from datetime import datetime
import os

app = Flask(__name__)

# Conexión a la Base de Datos
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'mysql'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'secret'
app.config['MYSQL_DATABASE_DB'] = 'sistema'
mysql.init_app(app)

CARPETA = os.path.join('uploads')
app.config['CARPETA'] = CARPETA

#Acceso a la carpeta Upload
@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(app.config['CARPETA'], nombreFoto)

# Creacion de las rutas
@app.route('/')
def index():
    sql = "SELECT * FROM empleados"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    empleados = cursor.fetchall()
    print(empleados)
    return render_template('empleados/index.html', empleados = empleados)

@app.route('/destroy/<int:id>')
def destroy(id):
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT foto FROM empleados WHERE idEmpleado = %s", id)
    fila = cursor.fetchall()
    #os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))

    cursor.execute("DELETE FROM empleados WHERE idEmpleado=%s", (id))
    conn.commit()
    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empleados WHERE idEmpleado=%s", (id))
    empleados = cursor.fetchall()
    return render_template('empleados/edit.html', empleados = empleados)

@app.route('/update', methods=['POST'])
def update():
    _nombre = request.form['txtNombre']
    _correo = request.form['txtCorreo']
    _foto = request.files['txtFoto']
    _id = request.form['txtID']

    sql = "UPDATE empleados SET nombre=%s, correo=%s WHERE idEmpleado=%s"
    datos = (_nombre, _correo, _id)

    conn = mysql.connect()
    cursor = conn.cursor()

    #now = datetime.now()
    #tiempo = now.strftime("%Y%H%M%S")
    #if _foto.filename != '':
    #    nuevoNombreFoto = tiempo + _foto.filename
    #    _foto.save("uploads/" + nuevoNombreFoto)
    #    cursor.execute("SELECT foto FROM empleados WHERE idEmpleado = %s", _id)
    #    fila = cursor.fetchall()

    #    os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))
    #    cursor.execute("UPDATE empleados SET foto=%s WHERE idEmpleado=%s", (nuevoNombreFoto, _id))
    #    conn.commit()
    cursor.execute(sql, datos)
    conn.commit()

    return redirect('/')

@app.route('/create')
def create():
    return render_template('empleados/create.html')

@app.route('/store', methods=['POST'])
def storage():
    _nombre = request.form['txtNombre']
    _correo = request.form['txtCorreo']
    _foto = request.files['txtFoto']

    #if _nombre == '' or _correo == '' or _foto == '':
    if _nombre == '' or _correo == '':
        flash('Recuerda llenar los datos de los campos')
        return redirect(url_for('create'))

    #now = datetime.now()
    #tiempo = now.strftime("%Y%H%M%S")
    #if _foto.filename != '':
    #    nuevoNombreFoto = tiempo + _foto.filename
    #    _foto.save("uploads/" + nuevoNombreFoto)

    sql = "INSERT INTO empleados (nombre, correo) VALUES (%s, %s)"
    datos = (_nombre, _correo)

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(host = "0.0.0.0",
            port = 4000,
            debug = True)
