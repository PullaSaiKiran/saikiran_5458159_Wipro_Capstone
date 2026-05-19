import logging
import os


class LogGen:

    @staticmethod
    def loggen():

        logger = logging.getLogger()

        if not logger.handlers:

            logger.setLevel(logging.INFO)

            base_dir = os.path.dirname(os.path.dirname(__file__))

            log_path = os.path.join(
                base_dir,
                "logs",
                "automation.log"
            )

            file_handler = logging.FileHandler(log_path)

            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s'
            )

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger