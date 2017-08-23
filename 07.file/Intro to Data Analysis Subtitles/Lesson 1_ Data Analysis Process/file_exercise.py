import os
import glob

file_list = glob.glob('*')

try:
    for file in file_list:
        if file.endswith('.txt'):
            os.remove(file + '..')
except Exception as err:
    print('no file', err)



