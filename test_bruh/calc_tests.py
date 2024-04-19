import unittest
import calc
import sys
 
class CalcBasicTests(unittest.TestCase):
     
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    @unittest.skipIf(sys.version_info < (3, 6),"Temporaly skip test_add") 
    def test_sub(self):
        self.assertEqual(calc.sub(4, 2), 2)
        
    def test_mul(self):
        self.assertEqual(calc.mul(2, 5), 10)
        
    def test_div(self):
        self.assertEqual(calc.div(8, 4), 2)

@unittest.skip("Temporaly skip test_add")
class CalcExTests(unittest.TestCase):
    
    def test_sqrt(self):
        self.assertEqual(calc.sqrt(4), 2)
           
    def test_pow(self):
        self.assertEqual(calc.pow(3, 3), 27)