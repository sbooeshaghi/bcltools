import binascii
import os
import sys


def is_gz_file(filepath):
    with open(filepath, 'rb') as test_f:
        return binascii.hexlify(test_f.read(2)) == b'1f8b'


def prepend_zeros_to_number(len_name, number):
    len_number = len(str(number))
    return '0' * (len_name - len_number) + str(number)


def get_bin(x, n=0):
    """
    Get the binary representation of x.

    Parameters
    ----------
    x : int
    n : int
        Minimum number of digits. If x needs less digits in binary, the rest
        is filled with zeros.

    Returns
    -------
    str
    """
    return format(x, 'b').zfill(n)


def qual2num(qual):
    num = ord(qual) - 33
    return num


def num2qual(num):
    qual = chr(num + 33)
    return qual


def clean_pipe(f, **args):
    try:
        f(**args)
    except BrokenPipeError:
        # Python flushes standard streams on exit; redirect remaining output
        # to devnull to avoid another BrokenPipeError at shutdown
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        sys.exit(1)  # Python exits with error code 1 on EPIPE


# def touch(file):
#     if not os.path.exists(file):
#         with open(file, 'w'): pass
