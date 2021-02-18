import unittest
from main import hello_world

class TestHelloWorld(unittest.TestCase):
    def test(self):
        expected = "Hello from Python!"
        result = hello_world()
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
