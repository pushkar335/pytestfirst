import logging


class Loggen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\logs\\orangehrm.log",
                            format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
