import sys
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    line_number = exc_tb.tb_lineno
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script: {file_name} at line number: {line_number} error message: {str(error)}"
    return error_message