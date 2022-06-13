"""task 1_d"""
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("src1", type=str, help="A string which contains a path to the file1")
parser.add_argument("src2", type=str, help="A string which contains a path to the file2")
parser.add_argument("dst", type=str, help="A string which contains a path where to save a new file")

args = parser.parse_args()
src1 = args.src1
src2 = args.src2
dst = args.dst
def file_opener(file_path):
    """
    str -> set
    Return set of strings, read from the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read()
        lines_data = set(lines.split('\n'))
        return lines_data

def files_compare(file1, file2):
    """
    (set, set)
    Create a file or return the message.
    """
    new_file = file1.intersection(file2)
    filepath = os.path.join(dst, 'new_file')
    if not os.path.exists(dst):
        os.makedirs(dst)
        file = open(filepath, 'w')
        for line in new_file:
            file.write(line)
        file.close()
    else:
        print("Cannot make a consisting directory")

if os.path.exists(src1) and os.path.exists(src2):
    file_1 = file_opener(src1)
    file_2 = file_opener(src2)
    files_compare(file_1, file_2)
else:
    print('There`s no file with such path')
