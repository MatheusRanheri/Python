import unittest
from function_calculos import soma, subtrair, multiplicar, dividir


class TestesFuncoes(unittest.TestCase):
    def testasoma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)

    def testasubtrair(self):
        self.assertEqual(subtrair(10, 4), 6)
        self.assertEqual(subtrair(0, 5), -5)

    def testamultiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(-2, 3), -6)

    def testadividir(self):
        self.assertEqual(dividir(8, 2), 4)
        self.assertEqual(dividir(9, 3), 3)
        self.assertEqual(dividir(5, 0), "Erro!!!")
        self.assertEqual(dividir(0, 5), "Erro!!!")


if __name__ == "__main__":
    unittest.main()
