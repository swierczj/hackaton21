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


def get_error_from_file(file):
    lines = file.readlines()
    error = str()
    exception_found = False
    for line in lines:
        splitted_line = line.split(' ')
        # delete colon in exception name
        if splitted_line[0][:-1] in python_built_in_exceptions:
            exception_found = True
        if exception_found:
            error += line
    return error


f = open("log.txt", "r")
err = get_error_from_file(f)
# print(f'{err}')
