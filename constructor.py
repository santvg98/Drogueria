class Deportista:
    def __init__(self, mysql):
        self.mysql = mysql
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor

    def consultar (self):
        sql =  f"SELECT * FROM inf_usuario"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def agregar(self, deport):
        sql = f"INSERT INTO inf_usuario(`id`, `nombre`, `estatura`, `peso`, `fecha_nacimiento`) VALUES ('{deport[1]}', '{deport[2]}', {deport[3]}, {deport[4]}, '{deport[5]}')"
        self.cursor.execute(sql)
        self.conexion.commit()

    def modificar(self, deport):
        sql = f"UPDATE `inf_usuario` SET `nombre`='{deport[1]}',`estatura`='{deport[2]}',`peso`='{deport[3]}',`fecha_nacimiento`='{deport[4]}' WHERE `id`='{deport[0]}'"
        self.cursor.execute(sql)
        self.conexion.commit()

    def borrar(self, id):
        sql = f"DELETE FROM `inf_usuario` WHERE id = {id}"
        self.cursor.execute(sql)
        self.conexion.commit()

    def buscar(self, id):
        sql = f"SELECT * FROM `inf_usuario` WHERE id = {id}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        if len(resultado) > 0:
            return True
        else:
            return False