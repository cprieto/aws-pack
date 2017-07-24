import argparse
from tempfile import mkdtemp
from lpack import process, default_filename

def main():
    parser = argparse.ArgumentParser(description='Package a Python AWS Lambda.')

    parser.add_argument('-r', '--requirements', 
        help='Pip requirement file, default is requirements.txt', 
        default='requirements.txt')

    parser.add_argument('-o', '--output',
        help='Output zip filename',
        default=default_filename())

    parser.add_argument('-t', '--tempdir', 
        help='Temporary directory to install dependencies', default=mkdtemp())

    parser.add_argument('-f', '--files', help='Files to include in package', nargs='+')
    
    args = parser.parse_args()

    process(args.files, args.requirements, args.tempdir, args.output)

