
def dec_with_args(function):
    def wrapper_accepting_arguments(arg1 : list):
        print(f"Org List: {arg1}")
        final_l = function(arg1)
        print(f"Conver list {final_l}")
    return wrapper_accepting_arguments

@dec_with_args
def min_sub_list(lst : list) ->list:
    res = []
    min_sum = float('inf')
    start, end = 0 , 0
    curr_start, curr_sum = 0 , 0
    for i in range(len(lst)):
        curr_sum += lst[i]
        if curr_sum < min_sum:
            min_sum = curr_sum
            start = curr_start
            end = i
        if curr_sum > 0:
            curr_sum = 0
            curr_start = i + 1
    
    return lst[start:end + 1]
	


def main():
    m_list = [1 ,2 , 10, 12]
    min_sub_list(m_list)
    
    m_list = [1 ,2 , 10, 12 , 4 ,-10, -11 , -9]
    min_sub_list(m_list)    


if __name__ == '__main__':
	main()