import unittest

from caesar_cipher import build_shift_dict


class TestStringMethods(unittest.TestCase):

    def build_shift_dict_test(self):
        value_for_a = build_shift_dict(3)["a"]
        self.assertEqual(value_for_a, "d")


if __name__ == '__main__':
    unittest.main()