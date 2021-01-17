from output_parse import get_output
import sys
import os
import subprocess
import parsing_output.parse_error
from libraries.requester import send_requests

if __name__ == "__main__":
    error_msg = get_output(sys.argv[1:])
    errors = parsing_output.parse_error.get_errors(error_msg)
    send_requests("stackoverflow.com", errors)
    os.system("start ./site/index.html")
    # print(f'{errors}')
