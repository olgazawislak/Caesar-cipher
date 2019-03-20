import unittest

from caesar_cipher import build_shift_dict, CiphertextMessage, apply_shift, load_words, WORDLIST_FILENAME


class TestMessageMethods(unittest.TestCase):

    def test_build_shift_dict(self):
        value_for_a = build_shift_dict(3)["a"]
        self.assertEqual(value_for_a, "d")

    def test_apply_shift(self):
        self.assertEqual(apply_shift("Hello!", 3), "Khoor!")

    def test_apply_shift_sentence(self):
        self.assertEqual(apply_shift("Hello! Nice to see you xyz.", 3), "Khoor! Qlfh wr vhh brx abc.")

    def test_decrypt_message_shift(self):
        encrypted_message = CiphertextMessage("Khoor!")
        self.assertEqual(encrypted_message.decrypt_message_shift(3), "Hello!")

    def test_decrypt_message_shift_sentence(self):
        encryp_message = CiphertextMessage("Khoor! Qlfh wr vhh brx abc.")
        self.assertEqual(encryp_message.decrypt_message_shift(3), "Hello! Nice to see you xyz.")

    def test_decrypt_message(self):
        message = CiphertextMessage("Khoor! Qlfh wr vhh brx abc.")
        self.assertEqual(message.decrypt_message(), (23, "Hello! Nice to see you xyz."))


if __name__ == '__main__':
    unittest.main()