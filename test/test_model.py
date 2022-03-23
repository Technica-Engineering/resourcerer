import unittest
from resourcerer.model import ResourcesYamlObj
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

    def test_yaml_obj_parsing_default(self):
        actual = ResourcesYamlObj.from_dict(self.yaml_dct_empty)
        expected = ResourcesYamlObj(
            [], [], "generic", Path(""), Path(""), "simple"
        )
        self.assertEqual(actual, expected)

    def test_yaml_obj_parsing_custom(self):
        actual = ResourcesYamlObj.from_dict(self.yaml_dct_custom)
        expected = ResourcesYamlObj(
            [Path("lol.txt")],
            [Path("rofl.txt")],
            "generic",
            Path("blah"),
            Path("blah")
        )
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
