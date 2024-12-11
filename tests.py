import unittest
from hello_world import get_info
class Tests(unittest.TestCase):
    def test_get_info(self):
        self.assertEqual(get_info('Alex'),'hello world fromAlex')

if __name__=='__main__':
    unittest.main()
