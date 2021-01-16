import subprocess
import sys


def compile(args):
    f = open("log.txt", "w")
    result = subprocess.run(args, shell=True, capture_output=True)
    f.write(str(result.stderr.decode("utf-8")))
    f.close()


if __name__ == "__main__":
    compile(sys.argv[1:])
