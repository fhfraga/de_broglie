import unittest
from scipy import constants
from core import de_broglie

massa_e = constants.m_e


class TestDeBroglie(unittest.TestCase):
    def test_e_v4e6(self):
        self.assertAlmostEqual(de_broglie.de_broglie_lambda(massa_e, 4e6),
                               1.8184737738719174e-10)


class TestDeEnergia(unittest.TestCase):
    def test_comp_onda_e(self):
        self.assertAlmostEqual(de_broglie.energia_de_foton(
            1.8184737738719174e-10), 1.092369795326876e-15)


class TestDeEnergiaMol(unittest.TestCase):
    def test_energia_foton(self):
        self.assertAlmostEqual(de_broglie.energia_de_foton_mol(
            1.092369795326876e-15), 657840477.5390708)
