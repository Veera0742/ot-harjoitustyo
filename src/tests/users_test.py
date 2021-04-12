import unittest 
from users import Users

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.user = Users("kukka", "auringonkukka")

    def test_username_and_password_is_set_correctly(self):
        self.assertEqual(str(self.user), "Tunnus: kukka, Salasana: auringonkukka, Status: Logged out")

    def test_username_and_password_works_if_correct(self):
        self.user.login("kukka", "auringonkukka")
        self.assertEqual(str(self.user), "Tunnus: kukka, Salasana: auringonkukka, Status: Logged in")

    def test_username_and_password_works_if_incorrect(self):
        self.user.login("kukka", "orvokki")
        self.assertEqual(str(self.user), "Tunnus: kukka, Salasana: auringonkukka, Status: Logged out")


