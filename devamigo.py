from output_parse import get_output
import sys
import os
import subprocess
import parsing_output.parse_error
from libraries.requester import send_requests
import libraries.utils as utils
from interactive_mode import get_interactive_answer
from libraries.utils import load_config

if __name__ == "__main__":
    load_config("config.json")
    returncode, stdout, stderr = get_output(sys.argv[1:])
    open_browser = utils.AUTO
    print(stdout)
    # if errors occured
    if returncode != 0:
        print("ERRORS")
        # print(stderr)
        errors = parsing_output.parse_error.get_errors(stderr)
        if len(errors) > 0:
            if not utils.AUTO:
                open_browser = get_interactive_answer(len(errors))
            if open_browser:
                send_requests(errors)
                os.system("start ./site/index.html")

