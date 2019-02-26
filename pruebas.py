import unittest
import funciones as f

class pruebas(unittest.TestCase):

    def test_calcular_precio_producto(self):
        self.assertEqual(f.calcular_precio_producto(1000), 1500)
        self.assertEqual(f.calcular_precio_producto(0), 0)

    def test_calcular_precio_servicio(self):
        self.assertEqual(f.calcular_precio_servicio(1000), 100000000)
        self.assertNotEqual(f.calcular_precio_servicio(3), 30000)
        self.assertEqual(f.calcular_precio_servicio(0), 0)

    def test_calcular_precio_servicio_extras(self):       
        self.assertEqual(f.calcular_precio_servicio_extras(1), 125000.0)
        self.assertEqual(f.calcular_precio_servicio_extras(3), 375000.0)
        self.assertNotEqual(f.calcular_precio_servicio_extras(0), 0.25)


    def test_calcular_costo_envio(self):
        self.assertEqual(f.calcular_costo_envio(1), 115)
        self.assertNotEqual(f.calcular_costo_envio(3), 315)
        self.assertEqual(f.calcular_costo_envio(0), 0)


    def test_calcular_precio_producto_fuera(self):
        self.assertEqual(f.calcular_precio_producto_fuera(2000,4), 3460)
        self.assertEqual(f.calcular_precio_producto_fuera(9000,50),19250)
        self.assertNotEqual(f.calcular_precio_producto_fuera(40,1), 615)

    def test_calcular_iva_producto(self):
        self.assertEqual(f.calcular_iva_producto(800,0.19), 228.0)
        self.assertNotEqual(f.calcular_iva_producto(0,0.19), 0.19)
        self.assertEqual(f.calcular_iva_producto(589621,0.19), 168041.98500000002)

    def test_calcular_iva_servicio(self):
        self.assertNotEqual(f.calcular_iva_servicio(0,0.19), 0.19)
        self.assertEqual(f.calcular_iva_servicio(800,0.19), 228.0)
        self.assertEqual(f.calcular_iva_servicio(589621,0.19), 168041.98500000002)

    def test_calcular_iva_envio(self):
        self.assertEqual(f.calcular_iva_servicio(5,0.19), 95000.0)
        self.assertEqual(f.calcular_iva_servicio(0,0.19), 0.0)
        self.assertNotEqual(f.calcular_iva_servicio(8,0.19), 800000.19)

    def test_calcular_iva_servicio_extra(self):
        self.assertNotEqual(f.calcular_iva_servicio_extra(8,0.19), 152000.0)
        self.assertEqual(f.calcular_iva_servicio_extra(3,0.19), 71250.0)
        self.assertEqual(f.calcular_iva_servicio_extra(9,0.19), 213750.0)

    def test_calcular_recaudo_locales(self):
        self.assertNotEqual(f.calcular_recaudo_locales(8,10,0), 0.0)
        self.assertEqual(f.calcular_recaudo_locales(3252,2000,5500), 16128.0)
        self.assertEqual(f.calcular_recaudo_locales(46000,0,15000), 91500.0)

    def test_calcular_recaudo_horas_extra(self):
        self.assertEqual(f.calcular_recaudo_horas_extra(1,9,9,7), 3250000)
        self.assertEqual(f.calcular_recaudo_horas_extra(4,0,25,21), 6250000)
        self.assertNotEqual(f.calcular_recaudo_horas_extra(2,0,1,9), 0)

    def test_calcular_recaudo_mixto_local(self):
        self.assertEqual(f.calcular_recaudo_horas_extra(1000,56900,5,3), 886850)
        self.assertEqual(f.calcular_recaudo_horas_extra(49500,5000,25,9), 3481750)
        self.assertNotEqual(f.calcular_recaudo_horas_extra(2,0,1,9), 0)


if __name__ == 'main':
    unittest.main()
