import argparse
import os
import sys

#create parser obj
parser = argparse.ArgumentParser(
                    prog='log-archive.py',
                    description='log-archive is utility for making backups of /var/log to /var/backup path with timestamp',
                    usage='%(prog)s [options]',
                    epilog='Project for roadmap.sh https://docs.python.org/3/library/argparse.html')

#add a few args
parser.add_argument("-c", "--compress", 
                    help="option to %(prog)s for compress type (default: %(default)s)", 
                    default="z", 
                    metavar="")

parser.add_argument("-d", 
                    "--delimiter", 
                    help="option to %(prog)s for delimiter for timestamp (default: %(default)s)", 
                    default="-", 
                    metavar="")

parser.add_argument("-v", 
                    "--verbose", 
                    help="option to %(prog)s for showing output during running command (default: %(default)s)", 
                    default=False,
                    action="store_true")

parser.add_argument("-t", 
                    "--target",
                     help="option to %(prog)s for path of archived folder (default: %(default)s)",
                     default="/var/log/", 
                     metavar="")

parser.add_argument("-b", 
                    "--backup", 
                    help="option to %(prog)s for path of folder to save backups (default: %(default)s)", 
                    default="/var/backup", 
                    metavar="")

parser.add_argument('--version', 
                    action='version', 
                    version='%(prog)s 0.1v')

#create tuple of args
args = parser.parse_args()


def choose_ext() -> str:
    """return tar extesnion corresponding to compression type"""
    try:
        if args.compress == "j":
            return ".tar.bz2"
        elif args.compress == "J":
            return ".tar.xz"
        elif args.compress == "z":
            return ".tar.gz"
        else:
            raise ValueError(f"No available key for tar compression: {args.compress}")
    except ValueError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

try:
    if not os.path.isdir(args.target):
        raise FileExistsError(f"No found directory for archive {args.target}")
except FileExistsError as e:
    print(f"ERROR: {e}")
    sys.exit(1)

if not os.path.isdir(args.backup):
    os.makedirs(args.backup)