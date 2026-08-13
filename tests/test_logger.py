import unittest
import logging

from src.logger import setup_logger


class TestSetupLogger(unittest.TestCase):

    def test_logger_is_created(self):
        logger = setup_logger()

        self.assertIsInstance(logger, logging.Logger)

    def test_logger_name(self):
        logger = setup_logger()

        self.assertEqual(logger.name, "battery_monitor")

    def test_logger_level(self):
        logger = setup_logger()

        self.assertEqual(logger.level, logging.INFO)


if __name__ == "__main__":
    unittest.main()