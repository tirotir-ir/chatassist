import unittest
from chatassist.utils import format_response, validate_api_key, load_api_key
import os


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.test_api_key_file = "test_api_key.txt"
        with open(self.test_api_key_file, "w") as f:
            f.write("test-valid-api-key")

    def tearDown(self):
        if os.path.exists(self.test_api_key_file):
            os.remove(self.test_api_key_file)

    def test_format_response(self):
        response = {"choices": [{"message": {"content": "Hello!"}}]}
        self.assertEqual(format_response(response), "Hello!")

        empty_response = {"choices": []}
        self.assertEqual(format_response(empty_response), "")

    def test_validate_api_key(self):
        with self.assertRaises(ValueError):
            validate_api_key("")
        with self.assertRaises(ValueError):
            validate_api_key("short")
        self.assertIsNone(validate_api_key("valid-api-key"))

    def test_load_api_key(self):
        api_key = load_api_key(self.test_api_key_file)
        self.assertEqual(api_key, "test-valid-api-key")

        with self.assertRaises(FileNotFoundError):
            load_api_key("nonexistent_key.txt")


if __name__ == "__main__":
    unittest.main()
