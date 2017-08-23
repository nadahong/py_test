import os, glob


for file in glob.glob('*'):
    if file.startswith('Lesson 1'):
        os.chdir(file)
        break

print('current dir: ' + os.getcwd())

for subtitle in glob.glob('*'):
    if subtitle.endswith('.txt'):
        os.remove(subtitle)
        print(subtitle + ' just removed..')

