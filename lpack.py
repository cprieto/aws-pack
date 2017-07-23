# -*- coding: utf-8 -*-
import pip
import sys
import zipfile
from platform import system
from tempfile import mkdtemp
from os import path, getcwd, walk, basename
from shutil import rmtree
import argparse

def install_dependencies(req_fname, on):
    if path.exists(req_fname):
        pip.main(['install', '-r', req_fname, '-t', on])

def clean(on):
    if path.isdir(on):
        rmtree(on)

def compress(on, output):
    zf = zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in walk(on):
        for f in files:
            fname = path.join(root, f)
            zf.write(fname, arcname=path.relpath(fname, on))
    zf.close()

def add_files(files, output):
    zf = zipfile.ZipFile(output, 'a', zipfile.ZIP_DEFLATED)
    for f in files:
        zf.write(f)
    zf.close()

def default_filename():
    fname = basename(getcwd()) + '.zip'
    return path.join(getcwd(), fname)

# TODO: It will be nice to support this as an external function
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
    req_fname = args.requirements

    try:
        install_dependencies(req_fname, args.tempdir)
        compress(args.tempdir, args.output)
        add_files(args.files, args.output)
    finally:
        clean(args.tempdir)

if __name__ == '__main__':
    main()
