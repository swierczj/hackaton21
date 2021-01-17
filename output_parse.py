import subprocess
import sys


def get_output(args):
    result = subprocess.run(args, shell=True, capture_output=True)
    program_stdout = str(result.stdout.decode("utf-8"))
    program_error = str(result.stderr.decode("utf-8"))
    return result.returncode, program_stdout, program_error

