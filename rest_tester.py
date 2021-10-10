import unittest
from test_auth import TestAuthenticationRestApi

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestAuthenticationRestApi)
	unittest.TextTestRunner().run(suite)
   
