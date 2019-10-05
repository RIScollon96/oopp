import tkinter as tk
from tkinter import filedialog


def read_oopp_file(file_path: str) -> dict:
    file = open(file_path, 'r')
    line = file.readline()

    oopp: dict = {}

    while line:
        key = line.strip()
        if key not in oopp:
            oopp[key] = {}
        line = file.readline().strip()
        dict_parts = line.split('=')
        name = dict_parts[1].strip()
        oopp[key][name] = {}
        line = file.readline()
        while '\t' in line:
            line.strip()
            dict_parts = line.split('=')
            oopp[key][name][dict_parts[0].strip()] = dict_parts[1].strip()
            line = file.readline()
    return oopp


def write_oopp_file(file_path: str, oopp: dict):
    file = open(file_path, 'w')
    for key in oopp:
        for key2 in oopp[key]:
            file.write(key + '\n')
            file.write('\t' + 'name = ' + key2 + '\n')
            for key3 in oopp[key][key2]:
                file.write('\t' + key3 + ' = ' + oopp[key][key2][key3] + '\n')


def select_file() -> str:
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    return file_path


def oopp_file_reader_test():
    file_path = select_file()

    oopp_dict = read_oopp_file(file_path)
    write_oopp_file('temp.txt', oopp_dict)

    oopp_dict = read_oopp_file('temp.txt')
    write_oopp_file('temp2.txt', oopp_dict)


oopp_file_reader_test()
