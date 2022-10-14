import os
import pprint


def read_file():
    path = os.getcwd() + '\Files/'
    folder_list = os.listdir(path)
    result = []
    for fail in folder_list:
        with open(path + fail, 'rt', encoding='utf8') as file:
            text = file.readlines()
            result.append([len(text), fail, "".join(text)])

    result.sort()
    with open("split_file.txt", 'w', encoding='utf8') as file_wr:
        for len_text, fail_name, text in result:
            file_wr.write(f"{fail_name}\n"
                          f"{len_text}\n"
                          f"{text}\n")



if __name__ == "__main__":
    read_file()
