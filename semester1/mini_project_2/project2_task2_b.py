"""task 2_b"""
import os
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("reg_expr", type=str, help="A regular expression to find files in directory")
parser.add_argument("path", type=str, help="A path to directory")

args = parser.parse_args()
regex = args.reg_expr
reg_exp = r'.{}'.format(regex)

dir_path = args.path

def file_extension(reg_e, path):
    """
    (str, str) -> list
    Return list with files, which have the regular expression.
    """
    tmp_list = []
    for element in os.walk(path):
        for files in element[2]:
            if re.search(reg_e, files):
                tmp_list.append(files)
    return tmp_list

if os.path.isdir(dir_path):
    final_list = file_extension(reg_exp, dir_path)
    if len(final_list) == 0:
        print("No matches found")
    else:
        for element in final_list:
            print(element)
else:
    print("There`s no such path or directory")
