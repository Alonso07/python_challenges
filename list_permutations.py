
def permutations(m_list):
    llen = len(m_list)
    if llen == 0:
        return []
    if llen == 1:
        return [m_list]
    result = []
    for i in range(llen):
        m = m_list[i]
        res_list = m_list[:i] + m_list[i+1:]
        for per in permutations(res_list):
            result.append([m] + per)
    return result



def main():
    my_list_1 = [1 ,2 ,3 ,4]
    print(f'Org list {my_list_1}')
    print(f'Per list {permutations(my_list_1)}')


if __name__ == "__main__":
	main()