class Producto():
    def __init__(self,nombre, precio, descripcion, cantidad, venta, cliente, compra):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.venta = venta
        self.cliente = cliente
        self.compra = compra 
        
    def get_json(self):
        return{
            "nombre":self.nombre,
            "precio":self.precio,
            "descripcion":self.descripcion,
            "cantidad":self.cantidad,
            "venta":self.venta,
            "cliente":self.cliente,
            "compra":self.compra,
        }
           
    def agregar_venta(self, venta, paciente, compra):
        self.venta = venta 
        self.paciente = paciente
        self.compra = compra    