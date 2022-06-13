import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="A string which contains a path to the directory")

args = parser.parse_args()

print('{}/'.format(os.path.basename(args.path)))

def print_dir(the_path, prefix=''):
    dirname = os.listdir(the_path)
    for item in dirname:
        elem_path = os.path.join(the_path, item)

        if os.path.isdir(elem_path):
            if item == dirname[-1]:
                print('{}└──  {}/'.format(prefix, item))
            else:
                print('{}├──  {}/'.format(prefix, item))
            print_dir(elem_path, prefix + '|  ')

        else:
            if item == dirname[-1]:
                print('{}└──  {}'.format(prefix, item))
            else:
                print('{}├──  {}'.format(prefix, item))


if not os.path.isdir(args.path):
    print('There`s no directory with such path.')
else:
    print_dir(args.path)