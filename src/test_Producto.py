import unittest


import producto


class TestProducto(unittest.TestCase):
	
    def test_sum(self):
        self.assertEqual(producto.sum(5, 7), 12)

    def setUp(self):
    	self.p = producto.Producto()
    def test_referencia(self):
    	self.assertEqual(self.p.set_referencia("0A28HG87FA"),0,"Referencia Insertada Correctamente")

    def test_nombre(self):
    	self.assertEqual(self.p.set_nombre("nvidia gtx"),0,"Nombre Insertado Correctamente")

    def test_descripcion(self):
    	self.assertEqual(self.p.set_descripcion("nvidia gtx grafica gaming"),0,"Descripcion Insertada Correctamente")


    def test_precio(self):
    	self.assertEqual(self.p.set_precio(105.4),0,"Precio Insertado Correctamente")
    def test_insercion_bd(self):
    	self.assertEqual(self.p.insercion_bd(),0,"Insertando en la base de datos")


    def test_render(self):
    	self.assertEqual(self.p.render(),0,"Mostrando plantilla")


if __name__ == "__main__":
    unittest.main()



