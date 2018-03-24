import unittest
import pysha2.sha256


class TestSha256(unittest.TestCase):

    def setUp(self):
        self.f = pysha2.sha256.hexdigest

    def test_empty(self):
        self.assertEqual(self.f(''),
                         'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855')

    def test_less_than_block_length(self):
        self.assertEqual(self.f('abc'),
                         'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad')

    def test_block_length(self):
        self.assertEqual(self.f('a'*64),
                         'ffe054fe7ae0cb6dc65c3af9b61d5209f439851db43d0ba5997337df154668eb')

    def test_several_blocks(self):
        self.assertEqual(self.f('a'*1000000),
                         'cdc76e5c9914fb9281a1c7e284d73e67f1809a48a497200e046d39ccc7112cd0')
