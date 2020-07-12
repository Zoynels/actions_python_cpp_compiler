#-*- coding: utf-8 -*-
import os
import sys
import glob
import subprocess
import zipfile
import json
import argparse


def install_dist(args):
    if str(args.func).lower() != "install_dist":
        return 0

    if args.pat is None:
        raise ValueError(f"Unknown 'pat' in args: {args}")

    if args.pkg_name is None:
        raise ValueError(f"Unknown 'pkg_name' in args: {args}")

    for fname in glob.glob(args.pat, recursive=True):
        subprocess.run(["python", "-m", "pip", "uninstall", "-y", args.pkg_name])
        subprocess.run(["python", "-m", "pip", "install", fname])
        sys.exit(0)
    raise RuntimeError("Can't find whl file in dist folder!")


def extractall(args):
    if str(args.func).lower() != "extractall":
        return 0

    if args.pat is None:
        raise ValueError(f"Unknown 'pat' in args: {args}")

    if args.dest_to is None:
        raise ValueError(f"Unknown 'dest_to' in args: {args}")
    
    for fname in glob.glob(args.pat, recursive=True):
        print(f"Found: {fname}")
        if not os.path.isfile(fname):
            continue
        with zipfile.ZipFile(fname, 'r') as zip_ref:
            print(f"Extract all from: {fname}")
            zip_ref.extractall(args.dest_to)


parser = argparse.ArgumentParser()
parser.add_argument('--func', help='function name')
parser.add_argument('--pat', help='pattern for function')
parser.add_argument('--dest_to', help='destination path')
parser.add_argument('--pkg_name', help='pkg_name for function')
args = parser.parse_args()

# util_funcs.py --func=extractall --pat=artifacts/** --dest_to=dist
extractall(args)
# util_funcs.py --func=install_dist --pat=dist/**.whl --pkg_name=actions_python_cpp_compiler
install_dist(args)
