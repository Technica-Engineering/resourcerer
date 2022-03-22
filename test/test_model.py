import unittest
from resourcerer.model import UnknownCachingStrategy, CachingStrategy, ResourcesYamlObj
from pathlib import Path


class TestModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.yaml_dct_custom = dict(
            download=["lol.txt"],
            upload=["rofl.txt"],
            root_source_dir="blah",
            target_dir="blah"
        )
        cls.yaml_dct_empty = dict()

    def test_caching_strategy_invalid_lookup(self):
        invalid_strategy = lambda: CachingStrategy.from_str("aasdfasdfa")
        self.assertRaises(UnknownCachingStrategy, invalid_strategy)

    def test_caching_strategy_valid(self):
        simple_caching_strat = CachingStrategy.from_str("SIMPLE")
        self.assertEqual(simple_caching_strat, CachingStrategy.SIMPLE)

    def test_yaml_obj_parsing_default(self):
        actual = ResourcesYamlObj.from_dict(self.yaml_dct_empty)
        expected = ResourcesYamlObj(
            [], [], Path(""), Path(""), CachingStrategy.SIMPLE
        )
        self.assertEqual(actual, expected)

    def test_yaml_obj_parsing_custom(self):
        actual = ResourcesYamlObj.from_dict(self.yaml_dct_custom)
        expected = ResourcesYamlObj(
            [Path("lol.txt")],
            [Path("rofl.txt")],
            Path("blah"),
            Path("blah")
        )
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
