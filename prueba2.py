import hashlib
import unittest 
class Foo(object):
	def gravatar_url(self, email):  
		hash = hashlib.md5(email.lower()).hexdigest()  
		return "https://www.gravatar.com/avatar/" + hash
class FooTestCase(unittest.TestCase):
	def setUp(self):
		self.foo = Foo() 
	def test_get_gravatar_url(self):
		result = self.foo.gravatar_url("example1@gmail.com")
		self.assertEquals(result, "https://www.gravatar.com/avatar/f3e820cc128ffde207328176830dff87")
 
if __name__ == "__main__":
	unittest.main()
