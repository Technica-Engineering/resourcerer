from pathlib import Path
import unittest
from resourcerer.caching import is_cached


class TestCaching(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.path_dir = Path(__file__).parent / Path("res")
        cls.filename_existing = "this_file_is_always_cached.txt"
        cls.filename_not_existing = "not_cached.txt"

    def test_is_cached(self):
        self.assertTrue(is_cached(self.filename_existing, self.path_dir))

    def test_is_not_cached(self):
        self.assertFalse(is_cached(self.filename_not_existing, self.path_dir))


if __name__ == "__main__":
    unittest.main()
