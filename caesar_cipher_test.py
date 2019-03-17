import unittest

from caesar_cipher import build_shift_dict, CiphertextMessage, apply_shift


class TestMessageMethods(unittest.TestCase):

    def test_build_shift_dict(self):
        value_for_a = build_shift_dict(3)["a"]
        self.assertEqual(value_for_a, "d")

    def test_apply_shift(self):
        self.assertEqual(apply_shift("Hello!", 3), "Khoor!")

    def test_decrypt_message_shift(self):
        encrypted_message = CiphertextMessage("Khoor!")
        self.assertEqual(encrypted_message.decrypt_message_shift(3), "Hello!")



if __name__ == '__main__':
    unittest.main()