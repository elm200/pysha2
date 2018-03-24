import unittest
import pysha2.sha384


class TestSha384(unittest.TestCase):

    def setUp(self):
        self.f = pysha2.sha384.hexdigest

    def test_empty(self):
        self.assertEqual(self.f(''),
                         '38b060a751ac96384cd9327eb1b1e36a21fdb71114be0743'+
                         '4c0cc7bf63f6e1da274edebfe76f65fbd51ad2f14898b95b')

    def test_less_than_block_length(self):
        self.assertEqual(self.f('abc'),
                         'cb00753f45a35e8bb5a03d699ac65007272c32ab0eded163'+
                         '1a8b605a43ff5bed8086072ba1e7cc2358baeca134c825a7')

    def test_block_length(self):
        self.assertEqual(self.f('a'*128),
                         'edb12730a366098b3b2beac75a3bef1b0969b15c48e2163c'+
                         '23d96994f8d1bef760c7e27f3c464d3829f56c0d53808b0b')

    def test_several_blocks(self):
        self.assertEqual(self.f('a'*1000000),
                         '9d0e1809716474cb086e834e310a4a1ced149e9c00f24852'+
                         '7972cec5704c2a5b07b8b3dc38ecc4ebae97ddd87f3d8985')
