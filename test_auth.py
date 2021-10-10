import requests
import unittest

class TestAuthenticationRestApi(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestAuthenticationRestApi, self).__init__(*args, **kwargs)
		self.__api_base_url = "http://localhost:5000"
		self.__secret_url = "/secret"
		self.__user_url = "/user"

	def test_auth_fail(self):
		r = requests.get(self.__api_base_url + "%s/%s/pwd/%s"%(self.__user_url, 'user', 'pass'))
		print(self.__api_base_url + "%s/%s/pwd/%s"%(self.__user_url, 'user', 'pass'))
		self.assertEqual(r.status_code, 403)

	def test_auth_default_user(self):
		r = requests.get(self.__api_base_url + "%s/%s/pwd/%s"%(self.__user_url, 'admin', 'root'))
		self.assertEqual(r.status_code, 201)

	def test_user_add(self):
		passwd = 'sampletestpasswd123'
		user = '/sluser'
		r = requests.post(self.__api_base_url + "%s/add/%s/pwd/%s"%(self.__user_url, user, passwd))
		self.assertEqual(r.status_code, 200)


	def test_user_change_passwd(self):
		passwd = 'samplenewpasswd123'
		user = '/sluser'
		r = requests.post(self.__api_base_url + "%s/%s/pwd/%s"%(self.__user_url, user, passwd))
		self.assertEqual(r.status_code, 200)

	def test_change_passwd_wrong_user(self):
		passwd = 'test'
		user = '/nosluser'
		r = requests.post(self.__api_base_url + "%s/%s/pwd/%s"%(self.__user_url, user, passwd))
		self.assertEqual(r.status_code, 403)

	def test_get_user_collection(self):
		self.test_user_add()
		r = requests.get(self.__api_base_url + self.__user_url)
		users = r.json()
		self.assertEqual("sluser" in users.keys(), True)
