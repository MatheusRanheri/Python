import unittest
import function_calculos as calculadora
from app import app


class TestesFuncoes(unittest.TestCase):
    def testasoma(self):
        self.assertEqual(calculadora.soma(2, 3), 5)
        self.assertEqual(calculadora.soma(-1, 1), 0)

    def testasubtrair(self):
        self.assertEqual(calculadora.subtrair(10, 4), 6)
        self.assertEqual(calculadora.subtrair(0, 5), -5)

    def testamultiplicar(self):
        self.assertEqual(calculadora.multiplicar(3, 4), 12)
        self.assertEqual(calculadora.multiplicar(-2, 3), -6)

    def testadividir(self):
        self.assertEqual(calculadora.dividir(8, 2), 4)
        self.assertEqual(calculadora.dividir(9, 3), 3)
        self.assertEqual(calculadora.dividir(5, 0), "Erro!!!")
        self.assertEqual(calculadora.dividir(0, 5), "Erro!!!")


class TestesAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_soma_api(self):
        response = self.app.get('/soma?a=2&b=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['resultado'], 5)

    def test_subtrair_api(self):
        response = self.app.get('/subtrair?a=10&b=4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['resultado'], 6)

    def test_multiplicar_api(self):
        response = self.app.get('/multiplicar?a=3&b=4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['resultado'], 12)

    def test_dividir_api(self):
        response = self.app.get('/dividir?a=8&b=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['resultado'], 4)

        response = self.app.get('/dividir?a=5&b=0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['resultado'], "Erro!!!")


if __name__ == "__main__":
    unittest.main()