

def list_creation():
    print("###List creation")
    m_list = ["test1" , "test2", "test3"]
    print(f"List {m_list}")
    m_list.append("test4")
    print(f"List {m_list}")
    m_list.insert(5, "test5")
    print(f"List {m_list}")
    return m_list

def list_deletion(m_list):
    print("###List deletion")
    ml = m_list
    ml.remove("test1")
    print(f"List {ml}")
    del ml[2]
    print(f"List {ml}")
	
def list_iteration(lst):
    print("###List iteration for in list")
    for ele in lst:
        print(f"Element {ele}")

def list_iteration2(lst):
    print("###List iteration for in range of len")
    for i in range(len(lst)):
        print(f'Element at {i} is {lst[i]}')


def main():
    ml = list_creation()
    list_iteration(ml)
    list_iteration2(ml)
    list_deletion(ml)

if __name__ == "__main__":
	main()