import logging
from datetime import datetime

class Logs:

    @staticmethod
    def Log_Gen(loglevel=logging.DEBUG,logger_name='Login_Logs'):
        logs = logging.getLogger(logger_name)
        logs.setLevel(loglevel)


        #creating a timestamp for the log filename
        dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # change format here
        #File handler setup
        log_file_path = f"C:\\Users\\shaik\\PycharmProjects\\pythonProject\\4_Keyword_Driven_Framework\\Logs\\LoginPage_{dt}.log"
        log_file = logging.FileHandler(log_file_path)
        file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%d-%m-%Y %I:%M:%S %p')
        log_file.setFormatter(file_format)

        # Add handlers to the logger
        logs.addHandler(log_file)
        return logs