import logging
from datetime import datetime


class Logs:
    @staticmethod
    def generate_log(loglevel=logging.DEBUG, logger_name="HRM Logs"):
        # This creates a logger instance named 'HRM Logs'
        logs = logging.getLogger(logger_name)
        logs.setLevel(loglevel)

        dt = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        log_file_path = f"C:\\Users\\User\\Desktop\\Practice\\ParaBank\\Logs\\Logfile_{dt}.log"
        log_file = logging.FileHandler(log_file_path)
        file_format = file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%m-%Y %I:%M:%S %p')
        log_file.setFormatter(file_format)

        logs.addHandler(log_file)

        return logs
