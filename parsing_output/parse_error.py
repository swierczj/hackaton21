from typing import List

python_built_in_exceptions = \
    [
        'AssertionError',
        'AttributeError',
        'EOFError',
        'FloatingPointError',
        'GeneratorExit',
        'ImportError',
        'ModuleNotFoundError',
        'IndexError',
        'KeyError',
        'KeyboardInterrupt',
        'MemoryError',
        'NameError',
        'NotImplementedError',
        'OSError',
        'OverflowError',
        'RecursionError',
        'ReferenceError',
        'RuntimeError',
        'StopIteration',
        'StopAsyncIteration',
        'SyntaxError',
        'IndentationError',
        'TabError',
        'SystemError',
        'SystemExit',
        'TypeError',
        'UnboundLocalError',
        'UnicodeError',
        'UnicodeEncodeError',
        'UnicodeDecodeError',
        'UnicodeTranslateError',
        'ValueError',
        'ZeroDivisionError'
    ]


def get_errors_from_file(file):
    lines = file.readlines()
    errors = []
    exception_found = False
    python_file = True
    for line in lines:
        splitted_line = line.split(' ')
        if is_java(splitted_line):
            errors.append(get_java_error(splitted_line))
        # get python file error
        elif python_file:
            if splitted_line[0][:-1] in python_built_in_exceptions:
                exception_found = True
            if exception_found:
                errors.append(line)
    return errors


def is_java(line: List[str]):
    return ".java:" in line[0]


def get_java_error(line: List[str]):
    error_found = False
    error_line = str()
    for word in line:
        if word == "error:":
            error_found = True
        if error_found:
            error_line += word + ' '
    error_line = error_line.rstrip()
    return error_line


f = open("java_log.txt", "r")
err = get_errors_from_file(f)
# test print
print(f'{err}')
