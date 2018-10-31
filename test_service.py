import unittest
from unittest.mock import patch, mock_open
from unittest import TestCase, mock
from service import Service

class Test_service(TestCase):

    # returns a random number
    # NOTE: You do not need to modify this method!
    # Mock it instead
    #def mock_bad_random():
     #   file_content = """12\n50\n20\n10\n30\n5"""
      #  mock_file = mock_open(read_data=file_content)

    # Test this
    def test_divide(self):
        ser = Service()
        ser.bad_random = mock.Mock(return_value=20)
        re = ser.divide(10)
        assert re == 2
        ser.bad_random = mock.Mock(return_value=20)
        re = ser.divide(-10)
        assert re == -2
        ser.bad_random = mock.Mock(return_value=20)
        self.assertRaises(ZeroDivisionError, ser.divide,0)       

    # Test this
    def test_abs_plus(self):
        ser = Service()
        re = ser.abs_plus(10)
        assert re == 11
        re = ser.abs_plus(-20)
        assert re == 21        

    # Test this
    def test_complicated_function(self):
        ser = Service()
        ser.bad_random = mock.Mock(return_value=15)
        re = ser.complicated_function(3)
        assert re == (5, 1)
        ser.bad_random = mock.Mock(return_value=15)
        self.assertRaises(ZeroDivisionError, ser.complicated_function,0)      