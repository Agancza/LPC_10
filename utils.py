from argparse import ArgumentParser


def parse_to_code():
    parser = ArgumentParser()
    parser.add_argument('-p', '--path', metavar='PATH', help='path to the .wav audio file')
    args = parser.parse_args()
    return args