"""task 1_b"""
import argparse
import os

def file_reader(txt_file):
    """
    Return string with the content of file.
    """
    with open(txt_file, 'r', encoding='utf-8') as file:
        contents = file.read()

    return contents

parser = argparse.ArgumentParser()
parser.add_argument("--inplace", help="To rewrite the file or just print", default="print")
parser.add_argument("str_to_be_ch", type=str, help="A string which has to be found and changed")
parser.add_argument("str_in_ch", type=str, help="A string, which has to be changed into")
parser.add_argument("path_to_file", type=str, help="A string with the path to the file")

args = parser.parse_args()
path_file = args.path_to_file
def string_replacement(str_to_be_ch, str_in_ch):
    old_string = file_reader(path_file)
    new_string = old_string.replace(str_to_be_ch, str_in_ch)

    return new_string

if os.path.exists(path_file):
    if args.inplace == "print":
        print(string_replacement(args.str_to_be_ch, args.str_in_ch))
    elif args.inplace == "rewrite":
        new_string = string_replacement(args.str_to_be_ch, args.str_in_ch)
        fr = open(path_file, 'w')
        fr.write(new_string)
        fr.close()
        print('Ready!')
    else:
        print("Enter 'rewrite' or keep --inplace empty")
else:
    print('There`s no file with such path')
