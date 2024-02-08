
"""


"""

def dict_creation():
    my_dict = dict()
    my_dict["1"] = 1
    print(f' Dictionary {my_dict}')
    my_dict_2 = {"data" : 1, "data2" : 4}
    print(f' Dict 2 {my_dict_2}')
    for i in range(20):
        my_dict[str(i)] = i
    return my_dict


def dict_delete(my_dic : dict) -> dict:
    del my_dic["15"]
    my_dic.popitem()
    my_dic.pop("17")
    return my_dic


def main():
    re_dict = dict_creation()
    print(re_dict)
    r2_dict = dict_delete(re_dict)
    print(r2_dict)

if __name__ == "__main__":
    main()
