import os
import tarfile
import parser_checker as pc #import module with overrided args via cli
import datetime
import shutil
import sys
import logging



def convert_size(size_bytes: int) -> str:
    """Convert to human-readable file size"""
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    unit_index = 0
    while size_bytes >= 1024 and unit_index < len(units) - 1:
        size_bytes /= 1024.0
        unit_index += 1
    return f"{size_bytes:.2f} {units[unit_index]}"

def create_fulname() -> str:
    """Create full name of tar file according to scheme log_archive_<date>.tar.<compression>"""
    date_time = str(datetime.datetime.now()).partition(".")[0].replace(" ", "_").replace("-", pc.args.delimiter).replace(":", pc.args.delimiter)
    full_name_tarfile = "log_archive_"+date_time+pc.choose_ext()
    return full_name_tarfile

def make_tarfile(full_name_tarfile: str, target_path: str):
    """"Create compressed tar and print its content if -v is given"""
    try:
        with tarfile.open(full_name_tarfile, "w:"+pc.choose_ext().split(".")[-1]) as tar:
            tar.add(target_path, arcname=".")
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        sys.exit(1)
        
    if pc.args.verbose == True:
        with tarfile.open(full_name_tarfile, "r") as tar:
            for member in tar.getmembers():
                print(member.name)

    return(f"{full_name_tarfile} size is {convert_size(os.stat(full_name_tarfile).st_size)}")

def main():
    """main func for calling others"""
    logging.basicConfig(level=logging.INFO)
    
    tar_file = create_fulname()
    logging.info(make_tarfile(tar_file, pc.args.target))
    shutil.move(tar_file, pc.args.backup)


if __name__ == "__main__":
    main()
