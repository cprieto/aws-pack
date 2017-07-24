# -*- coding: utf-8 -*-
import pip
import sys
import zipfile
from platform import system
from tempfile import mkdtemp
from os import path, getcwd, walk 
from shutil import rmtree

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
    fname = path.basename(getcwd()) + '.zip'
    return path.join(getcwd(), fname)

def process(files, req_fname='requirements.txt', tempdir=mkdtemp(), output=default_filename()):
    try:
        install_dependencies(req_fname, tempdir)
        compress(tempdir, output)
        add_files(files, output)
    finally:
        clean(tempdir)
