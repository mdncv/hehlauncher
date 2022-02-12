import os
import sys
import subprocess
import argparse


def parse_arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument('path', help='Show me da wae wer da file liez')

    parser.add_argument('-m', '--message', type=str, help='Da string I should add', default='heh')
    parser.add_argument('-p', '--position', type=int, help='Place wer I should add string',
                        default=0)

    args = parser.parse_args()

    return args.path, args.message + '\n', args.position


def exist_check(path):

    flag = True

    if not os.path.isfile(path):
        flag = input('There is no such file in directory, create new file?\ny/n:\n').lower() == 'y'
        if flag:
            open(path, 'w').close()

    return flag


def pos_check(path, pos, length):
    i = 0
    count = 0

    with open(path, 'r') as file:
        while i < length and count < pos:
            i += 1
            if file.read(1) == '\n':
                count += 1

    n = pos - count

    with open(path, 'a') as file:
        file.write('\n'*n)
        i += n

    return i


def heh(path, msg, pos):

    length = os.path.getsize(path)
    msg_length = len(msg)
    new_pos = pos_check(path, pos, length)

    with open(path, 'r+b') as file:
        for i in range(length - new_pos):
            file.seek(length - 1 - i)
            buffer = file.read(1)
            file.seek(length + msg_length - 1 - i)
            file.write(buffer)
        file.seek(new_pos)
        file.write(msg.encode('utf-8'))


def raise_notepad(path):

    if sys.platform == "win32":
        os.startfile(path)
    elif sys.platform == "darwin":
        opener = "open"
        subprocess.call([opener, path])
    else:
        opener = "xdg-open"
        subprocess.call([opener, path])


def main():

    path, msg, pos = parse_arguments()

    if exist_check(path):
        heh(path, msg, pos)
        raise_notepad(path)
    else:
        print('GLHF!')


if __name__ == '__main__':

    main()
