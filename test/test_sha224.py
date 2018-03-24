import unittest
import pysha2.sha224


class TestSha224(unittest.TestCase):

    def setUp(self):
        self.f = pysha2.sha224.hexdigest

    def test_empty(self):
        self.assertEqual(self.f(''),
                         'd14a028c2a3a2bc9476102bb288234c415a2b01f828ea62ac5b3e42f')

    def test_less_than_block_length(self):
        self.assertEqual(self.f('abc'),
                         '23097d223405d8228642a477bda255b32aadbce4bda0b3f7e36c9da7')

    def test_block_length(self):
        self.assertEqual(self.f('a'*64),
                         'a88cd5cde6d6fe9136a4e58b49167461ea95d388ca2bdb7afdc3cbf4')

    def test_several_blocks(self):
        self.assertEqual(self.f('a'*1000000),
                         '20794655980c91d8bbb4c1ea97618a4bf03f42581948b2ee4ee7ad67')
