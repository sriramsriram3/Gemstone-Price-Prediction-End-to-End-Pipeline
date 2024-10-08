import sys

class custom_ecxeption(Exception):
    def __init__(self,error_meassage,error_details:sys):
        self.error_message=error_meassage
        _,_,error_tb=error_details.exc_info()
        self.error_line=error_tb.tb_lineno
        self.file_name=error_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        return "error occured in python script [{0}] , in the line number [{1}] and error message is [{2}]".format(self.file_name,self.error_line,self.error_message)


if __name__ == '__main__':
    try:
        a=1/0

    except Exception as e :
        raise custom_ecxeption(e,sys)
    