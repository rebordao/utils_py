"""
Utils Class.
"""
from typing import List
import logging
import sys


class Utils:
    """
    A collection of utilities.
    """

    def __init__(self):
        return

    @staticmethod
    def init_logger(
            level: str, exclude: List, date_format='%Y%m%d %H:%M:%S',
            format='%(asctime)s %(levelname)s %(message)s') -> None:
        """
        Sets up and initialises logger.
        The loggers in the exclude list will have their level set to 'WARNING'
        """
        logging.basicConfig(
            stream=sys.stdout,
            format=format,
            datefmt=date_format,
            level=level
        )
        for ex in exclude:
            logging.getLogger(ex).setLevel(logging.WARNING)
        return

    @staticmethod
    def do_batches(alist, batch_size):
        """
        Returns a list of lists where each sublist has size batch_size.
        This is handy for multi GET and multi POST API requests.

        Example:
        For alist = [2, 3, 4, 1, 5, 5, 1] and batch_size = 3,
        the output is [[2, 3, 4], [1, 5, 5], [1]]
        """
        for i in range(0, len(alist), batch_size):
            if i + batch_size <= len(alist):
                yield alist[i:i + batch_size]
            else:
                yield alist[i:len(alist)]
