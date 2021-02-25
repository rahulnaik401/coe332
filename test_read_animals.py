import unittest
from read_animals import breed

class TestReadAnimals(unittest.TestCase):
	D1={'head':'lion', 'body':'calf-chimp','arms':10, 'legs':3, 'tail':13}
	D2={'head':'lion', 'body':'calf-chimp', 'arms':10, 'legs':3, 'tail':13}
	 
	def test_breed(self):
		self.assertDictEqual(breed(self.D1,self.D2),breed(self.D1,self.D2))

		self.assertRaises(AssertionError,breed,1)
    		self.assertRaises(AssertionError,breed,True)
    		self.assertRaises(AssertionError,breed,{})

if __name__=='__main__':
	unittest.main()
		
	
