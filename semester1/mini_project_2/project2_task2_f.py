"""task 2_f"""
import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('reg_exp_to_search', type=str, help='A string, which is a regular expression to search in files')
parser.add_argument('reg_extens', type=str, help='Regular expression to choose files')
parser.add_argument('--show_lines', '-sl', type=str, default='not show', help='Print number of string: string')
parser.add_argument('--only_show_counts', '-osc', type=str, default='not show', help='To show file name and number of strings with regular expression')

args = parser.parse_args()

direct = os.getcwd()
regex = args.reg_exp_to_search
extension = args.reg_extens
regular = r'.{}'.format(extension)
reg = r'\w*:'

def file_oper(file_path):
    """
    Return strings with the info, according to optional arguments.
    """
    if args.show_lines == 'show' and args.only_show_counts == 'show':
        print('Choose one optional argument')
    else:
        tmp = {}
        for file in os.listdir(file_path):
            if re.search(regular, file):
                tmp[file] = []
                with open(file, encoding='utf-8') as f:
                    lines = f.read()
                    list_lines = lines.split('\n')
                    for line in list_lines:
                        line_num = list_lines.index(line) + 1
                        line = '{}:{}'.format(line_num, line)
                        if re.search(regex, line):
                            tmp[file].append(line)
        for key,val in tmp.items():
            if len(val) == 0:
                continue
            if args.show_lines == 'not show' and args.only_show_counts == 'not show':
                print(key, end='\n')
                for line in val:
                    reg_def = re.search(reg, line)
                    line = line.replace(reg_def.group(0), "")
                    print(line, end='\n')
            if args.show_lines == 'show' and args.only_show_counts == 'not show':
                print(key, end='\n')
                for line in val:
                    print(line, end='\n')
            if args.show_lines == 'not show' and args.only_show_counts == 'show':
                print(key, len(val))
            
file_oper(direct)
