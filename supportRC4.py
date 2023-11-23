def DecToBin(dec):
	bin = [0, 0, 0, 0, 0, 0, 0, 0]
	for i in range(8):
		bin[7 - i] = dec % 2
		dec = int(dec / 2 )
	return bin;

def BinToHex(bin):
	x = 0
	for i in range(4):
		x = x + bin[i] * pow(2, 3 - i)
	if x < 10: 
		return chr(x + 48);
	else: 
		return chr(x + 87);

def Xor_DecToHex(a, b):
    abin = DecToBin(a)
    bbin = DecToBin(b)
    res = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        res[i] = abin[i] ^ bbin[i]
    result = ""
    result += BinToHex(res[0: 4])
    result += BinToHex(res[4: 8])
    return result;
