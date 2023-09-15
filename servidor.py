'''
Se trata de elaborar una aplicación web, enfatizando en el
backend, que conecte una base de datos mínima (dos tablas)
que gestione información de los deportistas del municipio
(id, nombre, estatura, peso, fecha de nacimiento, [opcional
foto]) y que además, cada que se haga una operación sobre
la tabla de deportistas se almacene que operación se llevó
a cabo, el id del deportista y la estampa de tiempo de dicha 
operación. El frontend debe ser mínimo.

El proyecto debe utilizar entorno virtual, en el cual solo
debe estar instalada la paquetería necesaria para su
funcionamiento.

El proyecto debe estar en un repositorio de github donde
también se coloque al final el comprimido con la base de
datos exportada.

El entregable es de esta actividad será la url del
repositorio creado en su cuenta personal de github
'''

from flask import Flask
from flaskext.mysql import MySQL

servidor = Flask(__name__)
mysql = MySQL()
servidor.config['MYSQL_DATABASE_HOST'] = 'localhost' 
servidor.config['MYSQL_DATABASE_PORT'] = 3306
servidor.config['MYSQL_DATABASE_USER'] = 'root'
servidor.config['MYSQL_DATABASE_PASSWORD'] = ''
servidor.config['MYSQL_DATABASE_DB'] = 'gestionclientes'
mysql.init_app(servidor)

if __name__ == '__main__':
    servidor.run(host = '0.0.0.0', debug = True, port = 5000)

    '''

asdfsfdsadfasdfasdf

    '''