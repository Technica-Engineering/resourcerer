from pathlib import Path
import argparse


def main():
    parser = argparse.ArgumentParser(description='Resource retrieval for CI testing')
    parser.add_argument('-f', '--file',
                        type=str,
                        help='Path to the Resources YAML file '
                             '(default is `resources.yaml` in the working directory)'
                        )
    parser.add_argument('-v', '--verbosity',
                        type=int,
                        help="What verbosity level to set (0 - 2), default = 1", default=1)



if __name__ == "__main__":
    main()
