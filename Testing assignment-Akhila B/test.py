import unittest
from validate import validate
from validate import check_card_type
class TestSum(unittest.TestCase):

    def test_me(self):
        num=79927398711
        res=validate(num)
        self.assertEqual(res,False)

    def test_me2(self):
        num=79927398713
        res=validate(num)
        self.assertEqual(res,True)

    def test_me3(self):
        num=79927398713
        res=validate(num)
        self.assertEqual(res,False)

    def test_me4(self):
        num=4111111111111111
        res=check_card_type(num)
        self.assertEqual(res,"visa")

    def test_me5(self):
        num=5500000000000004
        res=check_card_type(num)
        self.assertEqual(res,"visa")
        
    def test_me6(self):
        num=5500000000000004
        res=check_card_type(num)
        self.assertEqual(res,"mastercard")

    def test_me4(self):
        num=340000000000009
        res=check_card_type(num)
        self.assertEqual(res,"american_express")

if __name__=='__main__':
    unittest.main()
