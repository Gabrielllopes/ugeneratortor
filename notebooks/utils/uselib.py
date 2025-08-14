import sys
import os


def append_parent_dir_to_sys_path():
    sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))
