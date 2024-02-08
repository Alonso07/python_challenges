

def count_let_in_word(mlst: list, char_in : str) -> dict:
    ldict = dict()
    for word in mlst:
        ctr = 0
        for letter in word:    
            if char_in is letter:
                ctr += 1
        ldict[word] = ctr       
    return ldict


def main():
    m_lst = ["apple", "banana", "orange"]
    letter = "a"
    m_d = count_let_in_word(m_lst, letter)
    print(f'Result {m_d}')


if __name__ =="__main__":
	main()