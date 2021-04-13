import unittest
from analyses import *


class TestFunctions(unittest.TestCase):
    def test_num_vaccinated_by_age(self):
        num_vaccinated_by_age("../../covid19-opendata-vaccini/dati", "../../output_files/")

    def test_num_vaccinated_per_category(self):
        num_administrations_per_category("../../covid19-opendata-vaccini/dati", "../../output_files/")


if __name__ == '__main__':
    unittest.main()
