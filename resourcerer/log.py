import logging
from logging import StreamHandler
import sys

VERBOSITY_TRANSLATION = {
    0: logging.ERROR,
    1: logging.INFO,
    2: logging.DEBUG,
}

STDOUT_HANDLER = StreamHandler(sys.stdout)
STDOUT_HANDLER.setLevel(logging.WARNING)
STDERR_HANDLER = StreamHandler(sys.stderr)
STDERR_HANDLER.setLevel(logging.ERROR)


def add_handlers(logger: logging.Logger):
    """Adds sane-config STDOUT and STDERR handlers
    to the logger that the function is called with.
    """
    logger.addHandler(STDOUT_HANDLER)
    logger.addHandler(STDERR_HANDLER)
