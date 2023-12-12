import os
import datetime

class Logger:
    def __init__(self, log_directory):
        self.log_directory = log_directory
        self.log_file = self._create_log_file()

    def _create_log_file(self):
        # Ensure the log directory exists
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

        # Create a new log file with a timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        log_file_path = os.path.join(self.log_directory, f"log_{timestamp}.txt")
        return open(log_file_path, 'w')

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"[{timestamp}] {message}\n"
        self.log_file.write(formatted_message)
        self.log_file.flush()

    def close(self):
        self.log_file.close()
