import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.logger import logging
def error_message_detail(error, error_detail: sys):
    """
    Returns a detailed error message with file name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in Python script: [{file_name}] at line [{exc_tb.tb_lineno}] with message: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Custom exception class to wrap around Python exceptions with more context.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
if __name__ == "__main__":
    
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e, sys)    
         
