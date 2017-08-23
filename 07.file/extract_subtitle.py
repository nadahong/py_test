import glob
import os


def get_subtitle(file_name):
    sub_title_content = []

    tmp_line = ''

    file = open(file_name)
    for line in file:
        line = line.replace('\n', '')
        if len(line) < 3 and line.isnumeric():
            pass
        elif line.count(':') > 2 or line.count('-->') > 0:
            pass
        elif line == '':
            continue
        else:
            tmp_line += line + ' '
            if line.endswith('.') or line.endswith(',') or len(tmp_line) > 80:
                sub_title_content.append(tmp_line)
                tmp_line = ''

    file.close()
    return sub_title_content


def make_file_and_save(content, file_name, ext='txt'):

    with open(file_name + '.' + ext, 'a') as file:
        for line in content:
            file.write('%s\n' % line)


def clear_dir():
    file_list = glob.glob('*')

    for item in file_list:
        if item.endswith('.txt'):
            os.remove(item)


def main():

    os.chdir('./Intro to Data Analysis Subtitles')
    dir_list = glob.glob('*')
    os.chdir('./' + dir_list[0])

    print('current dir is : ' + os.getcwd())

    clear_dir()

    subtitle_list = glob.glob('*.srt')

    for file_name in subtitle_list:
        print(file_name, "is working..")
        subtitle_content = get_subtitle(file_name)
        make_file_and_save(subtitle_content, file_name, 'txt')

    print('job completed..')


if __name__ == '__main__':
    main()
