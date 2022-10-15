import unittest
import Unit_test

class FizzBazzTest(unittest.TestCase):

    def test_fizz(self):
        number =6
        
        result = Unit_test.get_reply(number)
        
        self.assertEqual(result,"Fizz")
        
    def  test_buzz(self):
    
        number = 10
        
        result = Unit_test.get_reply(number)
        
        self.assertEqual(result , "Buzz")
        
        
    def test_fizzbuzz(self):
        
        number = 15
        
        result = Unit_test.get_reply(number)

        self.assertEqual(result , "FizzBazz")
        
        
if __name__ == '__main__':
    unittest.main()