import unittest
import calculadora


class Testes(unittest.TestCase):

        def test_soma(self):
            self.assertEqual(calculadora.soma(2,3), 5)
            self.assertEqual(calculadora.soma(-1,1), 0)

        def test_subtrair(self):
            self.assertEqual(calculadora.subtrair(10, 4), 6)
            self.assertEqual(calculadora.subtrair(0, 5), -5)

        def test_multiplicar(self):
            self.assertEqual(calculadora.multiplicar(3, 4), 12)
            self.assertEqual(calculadora.multiplicar(-2, 3), -6)

        def test_dividir(self):
            self.assertEqual(calculadora.dividir(8, 2), 4)
            self.assertEqual(calculadora.dividir(9, 3), 3)
            self.assertEqual(calculadora.dividir(5, 0), "Erro!!!")


if __name__ == "__main__":
    unittest.main()