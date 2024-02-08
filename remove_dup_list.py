
def remove_dup(m_lst: list) -> list:
    m_dict = dict()
    ctr = 0
    res = [] ## use a new variable to store the result data!
    for i in range( len(m_lst) - 1):
        ele = m_lst[i]
        if ele in m_dict:
            i -= 1
        else:
            res.append(ele)
            m_dict[ele] = ele
    return res
    


def main():
	m_lst = [2, 1 ,3 ,4 , 5 , 1 ,2 ,3, 1, 5]
	print(f'Org list {m_lst}')
	print(f'Final list {remove_dup(m_lst)}')

if __name__ == '__main__':
	main()