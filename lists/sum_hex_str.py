

def sum_hex_str(hex1: str, hex2 : str) -> str:
    intres = int(hex1, 16) + int(hex2, 16)
    return hex(intres)


def main():
	hex_str1 = "0xFFFFFF"
	hex_str2 = "0x01"
	
	res = sum_hex_str(hex_str1, hex_str2)
	print(f"Result {res}")



if __name__ =="__main__":
	main()