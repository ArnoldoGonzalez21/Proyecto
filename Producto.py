class Producto():
    def __init__(self,nombre, precio, descripcion, cantidad, venta, cliente, compra, imagen):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.venta = venta
        self.cliente = cliente
        self.compra = compra 
        self.imagen = imagen
        
    def get_json(self):
        return{
            "nombre":self.nombre,
            "precio":self.precio,
            "descripcion":self.descripcion,
            "cantidad":self.cantidad,
            "venta":self.venta,
            "cliente":self.cliente,
            "compra":self.compra,
            "imagen":self.imagen
        }
           
    def agregar_venta(self, venta, cliente, compra):
        self.venta = venta 
        self.cliente = cliente
        self.compra = compra    