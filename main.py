from output_parse import get_output
import sys
import subprocess
import parsing_output.parse_error

if __name__ == "__main__":
    error_msg = get_output(sys.argv[1:])
    errors = parsing_output.parse_error.get_errors(error_msg)
    # print(f'{errors}')
