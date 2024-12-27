import unittest
import os
from chatassist.conversation import Conversation


class TestConversation(unittest.TestCase):
    def setUp(self):
        self.conversation = Conversation()
        self.test_file = "test_conversation.json"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_message(self):
        self.conversation.add_message("user", "Hello!")
        self.assertEqual(len(self.conversation.get_history()), 1)
        self.assertEqual(self.conversation.get_history()[0]["role"], "user")
        self.assertEqual(
            self.conversation.get_history()[0]["content"], "Hello!"
        )

    def test_save_and_load(self):
        self.conversation.add_message("user", "Hello!")
        self.conversation.add_message("assistant", "Hi there!")
        self.conversation.save_to_file(self.test_file)

        loaded_conversation = Conversation()
        loaded_conversation.load_from_file(self.test_file)
        self.assertEqual(
            self.conversation.get_history(), loaded_conversation.get_history()
        )


if __name__ == "__main__":
    unittest.main()
