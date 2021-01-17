from output_parse import get_output
import sys
import os
import subprocess
import parsing_output.parse_error
from libraries.requester import send_requests
from libraries.utils import load_config


if __name__ == "__main__":
    load_config("config.json")
    error_msg = get_output(sys.argv[1:])
    errors = parsing_output.parse_error.get_errors(error_msg)
    send_requests(errors)
    os.system("start ./site/index.html")
    # print(f'{errors}')
