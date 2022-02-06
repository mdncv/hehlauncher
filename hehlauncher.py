import os.path
import sys


def exist_check(path):
    check1 = os.path.isfile(path)
    check2 = False
    if not check1:
        check2 = input('There is no such file in directory, create new file?\ny/n: ') == 'y'
        if check2:
            open(path, 'w').close()
    return check1 or check2


def heh(filename):  # решение не подойдет для больших файлов
    with open(filename, 'r') as fin:
        buffer = fin.read()
    with open(filename, 'w') as fout:
        fout.write('heh\n' + buffer)


def raise_notepad(filename):
    exc1 = exc2 = True
    try:
        os_command_string = 'gedit ' + filename
        os.system(os_command_string)
    except:
        exc1 = False
    try:
        os_command_string = 'notepad.exe ' + filename
        os.system(os_command_string)
    except:
        exc2 = False
    if not exc1 and not exc2:
        nu = input('What is your notepad utility?\n')
        try:
            os_command_string = nu + ' ' + filename
            os.system(os_command_string)
        except:
            print('\nNo such utility, glhf!')


def main():
    filename = ''
    if len(sys.argv) == 1:
        filename = input('Filename empty, enter filename:\n')
    elif len(sys.argv) > 2:
        filename = input('Filename may be incorrect, enter correct filename:\n')
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
    if filename == '':
        print('\nFilename empty, glhf')
    elif exist_check(filename):
        heh(filename)
        raise_notepad(filename)
    else:
        print('\nglhf!')


if __name__ == '__main__':
    main()
