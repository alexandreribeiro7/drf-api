
import unittest

def dividir(a, b):
    if b == 0:
        return None
    return a / b


class TestDividir(unittest.TestCase):
    def test_dividir_por_1_retorna_mesmo_numero(self):
        self.assertEqual(dividir(5, 1), 5)
        self.assertEqual(dividir(1, 1), 1)
        
        
        
if __name__ == '__main__':
    unittest.main()