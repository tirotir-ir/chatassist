import unittest
from chatassist.api import ChatGPTAPI
from unittest.mock import patch, Mock


class TestChatGPTAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = "test-key"
        self.api = ChatGPTAPI(api_key=self.api_key)

    @patch("chatassist.api.requests.post")
    def test_send_message_success(self, mock_post):
        # Mock successful API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "choices": [{"message": {"content": "Hello, user!"}}]
        }
        mock_post.return_value = mock_response

        response = self.api.send_message("Hello, ChatGPT!")
        self.assertEqual(response, "Hello, user!")

    @patch("chatassist.api.requests.post")
    def test_send_message_failure(self, mock_post):
        # Mock API failure response
        mock_response = Mock()
        mock_response.status_code = 500
        mock_post.return_value = mock_response
        mock_post.side_effect = Exception("Internal Server Error")

        with self.assertRaises(Exception):
            self.api.send_message("Hello, ChatGPT!")


if __name__ == "__main__":
    unittest.main()
