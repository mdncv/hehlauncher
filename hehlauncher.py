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


def heh_buffer():
    buffer = 'hehbuffer.txt'
    n = 1
    if os.path.isfile(buffer):
        buffer = buffer[0:6] + str(n) + '.txt'
    while os.path.isfile(buffer):
        n += 1
        buffer = buffer[0:6] + str(n) + '.txt'
    open(buffer, 'w').close()
    return buffer


def heh(filename):  # решение не подойдет для больших файлов
    buffer_name = heh_buffer()
    with open(buffer_name, 'w') as hb_out:
        hb_out.write('heh\n')
        with open(filename, 'r') as fin:
            for line in fin:
                hb_out.write(line)
    with open(buffer_name, 'r') as hb_in:
        with open(filename, 'w') as fout:
            for line in hb_in:
                fout.write(line)
    os.remove(buffer_name)


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
    '''if filename[-4:] != '.txt':  #if we need txt file
        print('Not supported file format, .txt is expected.\nglhf!')
    el'''
    if filename == '':
        print('\nFilename empty, glhf')
    elif exist_check(filename):
        heh(filename)
        raise_notepad(filename)
    else:
        print('\nglhf!')


if __name__ == '__main__':
    main()
