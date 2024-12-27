import unittest
import subprocess
import os
from unittest.mock import patch


class TestCLI(unittest.TestCase):
    """
    Tests for the CLI functionality of the ChatAssist package.
    """

    def setUp(self):
        """
        Create a mock API key file before each test.
        """
        self.api_key_path = "test_api_key.txt"
        self.test_message = "Hello, ChatGPT!"
        self.mock_api_key = "test_key"

        # Create a mock API key file
        with open(self.api_key_path, "w") as f:
            f.write(self.mock_api_key)

    def tearDown(self):
        """
        Clean up the mock or real API key file after each test.
        """
        if os.path.exists(self.api_key_path):
            os.remove(self.api_key_path)

    @patch("chatassist.api.ChatGPTAPI.send_message")
    def test_cli_success(self, mock_send_message):
        """
        Test successful CLI interaction with a mocked API response.
        """
        # Mock the API response
        mock_send_message.return_value = "Hello! How can I assist you today?"

        # Run the CLI command
        result = subprocess.run(
            [
                "python",
                "-m",
                "chatassist.cli",
                self.test_message,
                "--api-key-path",
                self.api_key_path,
            ],
            capture_output=True,
            text=True,
        )

        # Check that the output matches the mocked response
        self.assertIn(
            "ChatGPT: Hello! How can I assist you today?",
            result.stdout,
        )

    def test_invalid_api_key_file(self):
        """
        Test CLI error when the API key file does not exist.
        """
        # Run the CLI command with a non-existent API key file
        result = subprocess.run(
            [
                "python",
                "-m",
                "chatassist.cli",
                self.test_message,
                "--api-key-path",
                "non_existent_key.txt",
            ],
            capture_output=True,
            text=True,
        )

        # Check the error output
        self.assertIn(
            "Error: API key file not found",
            result.stderr,
        )


if __name__ == "__main__":
    unittest.main()
