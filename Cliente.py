class Cliente():
    def __init__(self,nombre,apellido,nombre_usuario,password,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.nombre_usuario = nombre_usuario
        self.password = password
        self.telefono = telefono
    
    def get_json(self):
        return{
            "nombre":self.nombre,
            "apellido":self.apellido,
            "nombre_usuario":self.nombre_usuario,
            "password":self.password,
            "telefono":self.telefono
        }