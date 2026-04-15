import sys
# lets try logging
# from src.logger import logging

def error_message_detail(error, error_detail:sys): #error, and the error detail given by sys
        _,_,exc_tb=error_detail.exc_info() # error tracebook, kaha pe error hua hai, line number, file name
        file_name=exc_tb.tb_frame.f_code.co_filename # file name jaha pe error hua hai
        line_number=exc_tb.tb_lineno # line number jaha pe error hua hai
        error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name, line_number, str(error))
        # script name -> the python file jaha error hua hai,   line_number -> line number jaha error hua hai,   str(error) -> error message
        return error_message

class CustomException(Exception):
        def __init__(self,error_message,error_details:sys):
                super().__init__(error_message) # calling the constructor of the parent class
                self.error_message=error_message_detail(error_message,error_details) # error message detail is a function which will return the error message with file name, line number and error message

        def __str__(self):
                return self.error_message
        
# lets try logging
# if __name__=="__main__":
#         try:
#                 a=1/0
#         except Exception as e:
#                 logging.info("Zero se divide nahi munna")
#                 raise CustomException(e,sys)
        