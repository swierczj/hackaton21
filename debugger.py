import subprocess
import sys


def debug(args):
    f = open("error.log", "w")
    result = subprocess.run(args, shell=True, capture_output=True)
    f.write(result.stderr.decode("utf-8"))
    f.close()
    return result.stderr.decode("utf-8")


if __name__ == "__main__":
    debug(sys.argv[1:])
