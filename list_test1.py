def none_repeatible(my_list):
    my_dict = {}
    for ele in my_list:
        if ele in my_dict:
            my_dict[ele] +=1
        else:
            my_dict[ele] = 1
    for ele in my_list:
        if my_dict[ele] == 1:
            return ele

def main():
    my_list = [1 ,2, 3, 4, 5]
    none_repeat = none_repeatible(my_list)
    print(f'List pass {my_list}')
    print(f'None repeat {none_repeat}')
    
    my_list = [1 ,2, 1, 2, 5]
    none_repeat = none_repeatible(my_list)
    print(f'List pass {my_list}')
    print(f'None repeat {none_repeat}')

    my_list = [1 ,2, 1, 2, 5, 5]
    none_repeat = none_repeatible(my_list)
    print(f'List pass {my_list}')
    print(f'None repeat {none_repeat}')    


if __name__ == '__main__':
    main()