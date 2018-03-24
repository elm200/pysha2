__author__ = 'Thomas Dixon, Eiji Sakai'
__license__ = 'MIT'


from pysha2.sha256 import Sha256


def hexdigest(m):
    return Sha224(m).hexdigest()


class Sha224(Sha256):
    _h = (0xc1059ed8, 0x367cd507, 0x3070dd17, 0xf70e5939,
          0xffc00b31, 0x68581511, 0x64f98fa7, 0xbefa4fa4)
    _output_size = 7
    digest_size = 28
