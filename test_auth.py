import requests
import unittest

class TestAuthenticationRestApi(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestAuthenticationRestApi, self).__init__(*args, **kwargs)
		self.__api_base_url = "http://localhost:5000"
		self.__secret_url = "/secret"
		self.__user_url = "/user"

	def test_auth_fail(self):
		r = requests.get(self.__api_base_url + self.__secret_url, auth=('user', 'pass'))
		self.assertEqual(r.status_code, 401)

	def test_auth_default_user(self):
		r = requests.get(self.__api_base_url + self.__secret_url, auth=('admin', 'root'))
		self.assertEqual(r.status_code, 201)

	def test_user_add(self):
		payload = {'pwd': 'sampletestpasswd123'}
		user = '/sluser'
		r = requests.post(self.__api_base_url + self.__user_url + user, data=payload)
		self.assertEqual(r.status_code, 200)

	def test_user_change_passwd(self):
		payload = {'pwd': 'samplenewpasswd123'}
		user = '/sluser'
		pwd_url = '/pwd'
		r = requests.put(self.__api_base_url + self.__user_url + user + pwd_url, data=payload)
		self.assertEqual(r.status_code, 200)

	def test_user_change_passwd_incorrect(self):
		payload = {'pwd': 'samplenewpasswd123'}
		user = '/sluser'
		pwd_url = '/pwd'
		r = requests.post(self.__api_base_url + self.__user_url + user + pwd_url, data=payload)
		self.assertEqual(r.status_code, 405)

	def test_change_passwd_wrong_user(self):
		payload = {'pwd': 'test'}
		user = '/nosluser'
		pwd_url = '/pwd'
		r = requests.put(self.__api_base_url + self.__user_url + user + pwd_url, data=payload)
		self.assertEqual(r.status_code, 403)

	def test_get_user_collection(self):
        self.test_user_add()
		r = requests.get(self.__api_base_url + self.__user_url)
		users = r.json()
		self.assertEqual(users.has_key('sluser'), True)
