import subprocess
import sys


def get_output(args):
    result = subprocess.run(args, shell=True, capture_output=True)
    return str(result.stderr.decode("utf-8"))

