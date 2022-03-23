from pathlib import Path
import argparse
from resourcerer.model import ResourcesYamlObj, CliArgs, Config
from resourcerer.defaults import DEFAULT_FILE


def make_main():
    def closure():
        parser = argparse.ArgumentParser(description='Resource retrieval for CI testing')
        parser.add_argument('-f', '--file',
                            type=str,
                            help='Path to the Resources YAML file '
                                 '(default is `resources.yaml` in the working directory)',
                            default=DEFAULT_FILE)
        parser.add_argument('-v', '--verbosity',
                            type=int,
                            help="What verbosity level to set (0 - 2), default = 1", default=1)
        args = parser.parse_args()

        cli_args = CliArgs(
            Path(args.file),
            args.verbosity
        )

        yaml_file_config = ResourcesYamlObj.from_yaml(cli_args.file)

        config = Config(
            cli_args,
            yaml_file_config
        )

    return closure
