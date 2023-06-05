
import re
from other.words.common import system_type


def run():
    if system_type == "windows":
        cet4_path = "D:\ifeng\english-wordlists\CET4_edited.txt"
        cet6_path = "D:\ifeng\english-wordlists\CET6_edited.txt"
        cet46_path = "D:\ifeng\english-wordlists\CET_4+6_edited.txt"
    else :
        pass

    cet4_data = do_file_to_dict(cet4_path)
    cet6_data = do_file_to_dict(cet6_path)
    cet46_data = do_file_to_dict(cet46_path)

    cet4_word_list = list(cet4_data.keys())
    cet6_word_list = list(cet6_data.keys())
    cet46_word_list = list(cet46_data.keys())

    cet4_set = set(cet4_word_list)
    cet6_set = set(cet6_word_list)
    cet46_set = set(cet46_word_list)

    print(f"cet4 word size: {len(cet4_set)}, {cet4_word_list[0:5]}")
    print(f"cet6 word size: {len(cet6_set)}, {cet6_word_list[0:5]}")
    print(f"cet46 word size: {len(cet46_set)}, {cet46_word_list[0:5]}")

    print()

def do_file_to_dict(path: str):
    dic = {}
    rule = re.compile("^[a-zA-Z]{1}.*$")
    with open(path, "r", encoding="utf-8") as f:
        count = 0
        for line in f.readlines():
            count += 1
            if len(line) > 0:
                line = line.replace('\n', '').replace("\r", "")
                splits = line.split(" ")
                if rule.match(splits[0]) is not None:
                    dic[splits[0]] = line
                    # print(splits[0])
                    # print(splits[1])
    return dic


if __name__ == '__main__':
    run()
