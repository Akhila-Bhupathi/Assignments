Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:\Users\ACER\Desktop\ValidateCreditCard\test.py ==========
..F.F.
======================================================================
FAIL: test_me3 (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\ACER\Desktop\ValidateCreditCard\test.py", line 19, in test_me3
    self.assertEqual(res,False)
AssertionError: True != False

======================================================================
FAIL: test_me5 (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\ACER\Desktop\ValidateCreditCard\test.py", line 29, in test_me5
    self.assertEqual(res,"visa")
AssertionError: 'mastercard' != 'visa'
- mastercard
+ visa


----------------------------------------------------------------------
Ran 6 tests in 0.098s

FAILED (failures=2)
>>> 