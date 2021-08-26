from json import dump
from itertools import zip_longest

with open("user.csv", "r", encoding="utf-8") as hobby:
    with open("hobby.csv", "r", encoding="utf-8") as hobby:
        all_list = zip_longest((" ".join(us.split(",")) for us in Users), hobby, fillvalue=None)
        my_dict = {str(el[0]).strip() : (el[1].strip()) if el[0] else exit(1) for el in all_list}

        with open('dict_n_h.json', 'w', encoding="utf-8") as f :
            dump(my_dict, f, ensure_ascii=False, indent=4)
            print(my_dict)
