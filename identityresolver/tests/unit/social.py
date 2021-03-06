import unittest, os
from ...social import SocialProfileResolver,ResolvedPerson

# from mock import patch 
# @mock.patch('requests.get', mock.Mock(side_effect = lambda k:{'aurl': 'a response', 'burl' : 'b response'}.get(k, 'unhandled request %s'%k) ))

class TestTwitterScraper(unittest.TestCase):

	def setUp(self):

		self.resolver = SocialProfileResolver()
		self.test_set = [ResolvedPerson(0,full_name = 'Moritz Gellner', city='Evanston',state='IL', age = '22'),
						 ResolvedPerson(1,full_name = 'Al Johri', city='Chicago',state='IL',age = '21'),
						 ResolvedPerson(2,full_name = 'Carson H. Potter', city='Chicago',state='IL', age = '23'),
						 ResolvedPerson(3,full_name = 'Daniel Thirman', city='Wilmette',state='IL', age = '21')]

	def test_from_csv_1(self):

		resolved_people = self.resolver._load_from_csv(os.getcwd() + '/identityresolver/tests/unit/test_identities_1.csv', 
													   city=1,state=2,age=3)

		print resolved_people

		self.assertEqual(self.test_set,resolved_people)

	def test_resolve(self):
		self.resolver.resolve(self.test_set)
		self.assertEqual(True,True)

if __name__ == "__main__":
	unittest.main()