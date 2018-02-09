#!/usr/bin/env python3

import argparse
import os
import os.path
import subprocess
import sys

_PREFIX="su17-"
_SUFFIX=""

class DirPathError(ValueError):
    def __init__(self, path, *args, **kwargs):
        self.path = path
        msg = "{} is not a path to a directory".format(path)
        ValueError.__init__(self, msg, *args, **kwargs)

def _dirpath(dirpath):
    dirpath = os.path.join(dirpath, '')
    if not os.path.isdir(dirpath):
        raise DirPathError(dirpath)
    return dirpath

def _jobname(args):
    dirname = os.path.dirname(args.dirpath)
    return args.prefix + dirname + args.suffix

def _cmd(dirpath):
    dirname = os.path.dirname(dirpath)[1:]
    return "".join([
        "\\newcommand\\dirpath[0]{{{}}}".format(dirpath),
        "\\newcommand\\dirname[0]{{{}}}".format(dirname),
        r"\input{master}"
        ])

def _outpath(args, jobname):
    if args.release:
        files = os.listdir(args.dirpath)
        jobname += '-v'
        files = [f for f in files if f.startswith(jobname)]
        if len(files) == 0:
            vText = '1'
        else:
            maxFile = os.path.splitext(max(files))[0]
            currentVText = maxFile[len(jobname):]
            currentV = int(currentVText)
            nextV = currentV + 1
            vText = str(nextV)
        jobname += vText
    return os.path.join(args.dirpath, jobname + '.pdf')

def _execute(args):
    args.dirpath = _dirpath(args.dirpath)
    jobname = _jobname(args)
    cmd = _cmd(args.dirpath)
    outpath = _outpath(args, jobname)

    latexrunpath = os.path.join(os.path.dirname(__file__), 'latexrun')
    p = subprocess.Popen(
        [latexrunpath,
            '--latex-args', "-shell-escape -jobname {}".format(jobname),
            '-Wall',
            '-o', outpath,
            cmd])
    return p.wait(3)

def _parse_args():
    arg_parser = argparse.ArgumentParser(
        description = "Weave together an exercise set.")
    arg_parser.add_argument(
        "dirpath", help="the directory containing the exercise set")
    arg_parser.add_argument(
        "--prefix", default=_PREFIX,
            help="output filename prefix(default: {})".format(_PREFIX))
    arg_parser.add_argument(
        "--suffix", default=_SUFFIX,
            help="output filename suffix(default: {})".format(_SUFFIX))
    arg_parser.add_argument(
        "--release", action='store_true',
            help="make a release of the exercise set")

    return arg_parser.parse_args()

def main():
    args = _parse_args()
    try:
        sys.exit(_execute(args))
    except DirPathError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
