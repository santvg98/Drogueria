from datetime import datetime


class Deportista:
    def __init__(self, mysql):
        self.mysql = mysql
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()

    def registrar_auditoria(self, id_deportista): 
        registro_tiempo = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = f"INSERT INTO auditoria (id_deportista, registro_tiempo) VALUES ('{id_deportista}', '{registro_tiempo}')"
        self.cursor.execute(sql)
        self.conexion.commit()

    def consultar (self):
        sql =  f"SELECT * FROM inf_usuario"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def agregar(self, deport):
        sql = f"INSERT INTO inf_usuario(id, nombre, estatura, peso, fecha_nacimiento) VALUES ('{deport[0]}', '{deport[1]}', {deport[2]}, {deport[3]}, '{deport[4]}')"
        self.cursor.execute(sql)
        self.conexion.commit()
        id_deportista = deport[0]
        self.registrar_auditoria(id_deportista)

    def modificar(self, deport):
        sql = f"UPDATE inf_usuario SET nombre='{deport[1]}',estatura='{deport[2]}',peso='{deport[3]}',fecha_nacimiento='{deport[4]}' WHERE id='{deport[0]}'"
        self.cursor.execute(sql)
        self.conexion.commit()

        id_deportista = deport[0]
        self.registrar_auditoria(id_deportista)

    def borrar(self, id):
        sql = f"DELETE FROM inf_usuario WHERE id = {id}"
        self.cursor.execute(sql)
        self.conexion.commit()
        
        self.registrar_auditoria(id)

    def buscar(self, id):
        sql = f"SELECT * FROM inf_usuario WHERE id = {id}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        if len(resultado) > 0:
            return True
        else:
            return False
        

