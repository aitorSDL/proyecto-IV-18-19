
def sum(a, b):
    for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError
    return a + b

class Producto:
	def set_referencia(self, referencia):
		if(len(referencia)>0):
			self.referencia=referencia
			return 0
		else:
			return 1
	def set_nombre(self, nombre):
		if(len(nombre)>0):
			self.nombre = nombre
			return 0
		else:
			return 1

	def set_descripcion(self, descripcion):
		if(len(descripcion) > 0):
			self.descripcion = descripcion
			return 0
		else:
			return 1
	def set_precio(self, precio):
		if(precio >= 0 and float(precio)):
			self.precio = precio
			return 0
		else:
			return 1
	def render(self):
		return 0
	def insercion_bd(self):
		return 0

