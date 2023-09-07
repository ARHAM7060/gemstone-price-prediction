import sys   #This module provides access to some variables used or maintained by the interpreter   
from src.logger import logging

def error_message_detail(error,error_detail:sys):  #error and system error in the form of error_detail are parameters
    _,_,exc_tb = error_detail.exc_info()           #exc_info() - returns the old-style representation of the handled exception
                                                   #returns the tuple (type(e), e, e.__traceback__) , e - exxception
    file_name = exc_tb.tb_frame.f_code.co_filename 

    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)                    #inheriting the error message from parent class(Exception)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):              #this function used to print the error_message whenever we print this customeexception class
        return self.error_message   
    
