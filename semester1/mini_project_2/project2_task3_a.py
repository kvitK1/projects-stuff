import os
import argparse
import re
import zipfile

# parser = argparse.ArgumentParser()
# parser.add_argument('')
# parser.add_argument()
# parser.add_argument()

# args = parser.parse_args()
dir_path = os.getcwd() # seond argument
e = r'.*.py' # first arg

def zip_opener(zip_f):
    list_of_file_names = []
    with zipfile.ZipFile(zip_f, 'r') as my_zip:
        list_of_file_names = my_zip.namelist()
        for file in list_of_file_names:
            if re.search('__MACOSX', file):
                continue
            if re.search(e, file):
                my_zip.extract(file)
                os.mkdir('tmp') # if isdir ... if not: create
                in_name = os.path.join('tmp', os.path.basename('new_archive') + '.zip')
                with zipfile.ZipFile(in_name, 'w') as zipObj:
                        zipObj.write(file)
                os.remove(file)

for file in os.listdir(dir_path):
    if zipfile.is_zipfile(file):
        zip_opener(file)
