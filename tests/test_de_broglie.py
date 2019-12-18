import unittest
from scipy import constants
from core import de_broglie

massa_e = constants.m_e

class TestDeBroglie(unittest.TestCase):
    def test_e_v4e6 (self):
        self.assertAlmostEqual(de_broglie.de_broglie_lambda(massa_e, 4e6), 1.8184737738719174e-10)