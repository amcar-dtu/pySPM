import unittest

import pyspm


class TestElts(unittest.TestCase):
    def test_basic(self):
        assert pyspm.utils.simplify_formula("H^29SiH") == "H2^29Si"
        assert pyspm.utils.get_mass("C") == 12
        assert pyspm.utils.is_main_isotope("C", 12)
        assert not pyspm.utils.is_main_isotope("C", 13)


if __name__ == "__main__":
    unittest.main()
