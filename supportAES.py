def HexToBin(hex):
	bin = [0, 0, 0, 0]
	x = 0
	if ord(hex) > 57:
		x = ord(hex.upper()) - 55
	else: 
		x = ord(hex) - 48
	for i in range(4):
		bin[3 - i] = x % 2
		x = int(x / 2 )
	return bin;
	
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
		
def BinToDec(bin):
	x = 0
	for i in range(8):
		x = x + bin[i] * pow(2, 7 - i)
	return x;

def LeftShift(bin, n):
	binShift = bin
	for i in range(n):
		binShift.append(binShift.pop(0))
	return binShift;


Sbox = [
["63", "7c", "77", "7b", "f2", "6b", "6f", "c5", "30", "01", "67", "2b", "fe", "d7", "ab", "76"],
["ca", "82", "c9", "7d", "fa", "59", "47", "f0", "ad", "d4", "a2", "af", "9c", "a4", "72", "c0"],
["b7", "fd", "93", "26", "36", "3f", "f7", "cc", "34", "a5", "e5", "f1", "71", "d8", "31", "15"],
["04", "c7", "23", "c3", "18", "96", "05", "9a", "07", "12", "80", "e2", "eb", "27", "b2", "75"],
["09", "83", "2c", "1a", "1b", "6e", "5a", "a0", "52", "3b", "d6", "b3", "29", "e3", "2f", "84"],
["53", "d1", "00", "ed", "20", "fc", "b1", "5b", "6a", "cb", "be", "39", "4a", "4c", "58", "cf"],
["d0", "ef", "aa", "fb", "43", "4d", "33", "85", "45", "f9", "02", "7f", "50", "3c", "9f", "a8"],
["51", "a3", "40", "8f", "92", "9d", "38", "f5", "bc", "b6", "da", "21", "10", "ff", "f3", "d2"],
["cd", "0c", "13", "ec", "5f", "97", "44", "17", "c4", "a7", "7e", "3d", "64", "5d", "19", "73"],
["60", "81", "4f", "dc", "22", "2a", "90", "88", "46", "ee", "b8", "14", "de", "5e", "0b", "db"],
["e0", "32", "3a", "0a", "49", "06", "24", "5c", "c2", "d3", "ac", "62", "91", "95", "e4", "79"],
["e7", "c8", "37", "6d", "8d", "d5", "4e", "a9", "6c", "56", "f4", "ea", "65", "7a", "ae", "08"],
["ba", "78", "25", "2e", "1c", "a6", "b4", "c6", "e8", "dd", "74", "1f", "4b", "bd", "8b", "8a"],
["70", "3e", "b5", "66", "48", "03", "f6", "0e", "61", "35", "57", "b9", "86", "c1", "1d", "9e"],
["e1", "f8", "98", "11", "69", "d9", "8e", "94", "9b", "1e", "87", "e9", "ce", "55", "28", "df"],
["8c", "a1", "89", "0d", "bf", "e6", "42", "68", "41", "99", "2d", "0f", "b0", "54", "bb", "16"]]

Rcon = [["01","00","00", "00"], ["02", "00", "00", "00"], ["04", "00", "00", "00"], ["08", "00", "00", "00"], ["10", "00", "00", "00"],
["20", "00", "00", "00"], ["40", "00", "00", "00"], ["80", "00", "00", "00"], ["1b", "00", "00", "00"], ["36", "00", "00", "00"]]

MixCol = [["02", "03", "01", "01"], ["01", "02", "03", "01"], ["01", "01", "02", "03"], ["03", "01", "01", "02"]]

MixCol1 = [["0e", "0b", "0d", "09"], ["09", "0e", "0b", "0d"], ["0d", "09", "0e", "0b"], ["0b", "0d", "09", "0e"]]

Sbox1 = [
["52", "09", "6a", "d5", "30", "36", "a5", "38", "bf", "40", "a3", "9e", "81", "f3", "d7", "fb"], 
["7c", "e3", "39", "82", "9b", "2f", "ff", "87", "34", "8e", "43", "44", "c4", "de", "e9", "cb"],
["54", "7b", "94", "32", "a6", "c2", "23", "3d", "ee", "4c", "95", "0b", "42", "fa", "c3", "4e"],
["08", "2e", "a1", "66", "28", "d9", "24", "b2", "76", "5b", "a2", "49", "6d", "8b", "d1", "25"],
["72", "f8", "f6", "64", "86", "68", "98", "16", "d4", "a4", "5c", "cc", "5d", "65", "b6", "92"],
["6c", "70", "48", "50", "fd", "ed", "b9", "da", "5e", "15", "46", "57", "a7", "8d", "9d", "84"],
["90", "d8", "ab", "00", "8c", "bc", "d3", "0a", "f7", "e4", "58", "05", "b8", "b3", "45", "06"],
["d0", "2c", "1e", "8f", "ca", "3f", "0f", "02", "c1", "af", "bd", "03", "01", "13", "8a", "6b"],
["3a", "91", "11", "41", "4f", "67", "dc", "ea", "97", "f2", "cf", "ce", "f0", "b4", "e6", "73"],
["96", "ac", "74", "22", "e7", "ad", "35", "85", "e2", "f9", "37", "e8", "1c", "75", "df", "6e"],
["47", "f1", "1a", "71", "1D", "29", "c5", "89", "6f", "b7", "62", "0e", "aa", "18", "be", "1b"],
["fc", "56", "3e", "4b", "c6", "d2", "79", "20", "9a", "db", "c0", "fe", "78", "cd", "5a", "f4"],
["1f", "dd", "a8", "33", "88", "07", "c7", "31", "b1", "12", "10", "59", "27", "80", "ec", "5f"],
["60", "51", "7f", "a9", "19", "b5", "4a", "0d", "2d", "e5", "7a", "9f", "93", "c9", "9c", "ef"],
["a0", "e0", "3b", "4d", "ae", "2a", "f5", "b0", "c8", "eb", "bb", "3c", "83", "53", "99", "61"], 
["17", "2b", "04", "7e", "ba", "77", "d6", "26", "e1", "69", "14", "63", "55", "21", "0c", "7d"]]

def Xor(x, y):
	xbin = []
	if len(x) < 2: 
		x = "0" + x
	xbin.extend(HexToBin(x[0]))
	xbin.extend(HexToBin(x[1]))
	ybin = []
	if len(y) < 2: 
		y = "0" + y
	ybin.extend(HexToBin(y[0]))
	ybin.extend(HexToBin(y[1]))
	for i in range(8):
		xbin[i] = xbin[i] ^ ybin[i]
	res = ""
	res += BinToHex(xbin[0:4])
	res += BinToHex(xbin[4:8])
	xbin.clear()
	ybin.clear()
	return res;

def Mul(x, y):
	ybin = []
	ybin.extend(HexToBin(y[0]))
	ybin.extend(HexToBin(y[1]))
	res = [0, 0, 0, 0, 0, 0, 0, 0]
	H1b = [0, 0, 0, 1, 1, 0, 1, 1]
	for i in range(8):
		if ybin[i] == 1:
			xbin = []
			xbin.extend(HexToBin(x[0]))
			xbin.extend(HexToBin(x[1]))
			for j in range(7 - i):
				msb = xbin.pop(0)
				xbin.append(0)
				if msb == 1:
					for k in range(8): 
						xbin[k] ^= H1b[k]
		else:
			xbin = [0, 0, 0, 0, 0, 0, 0, 0]
		c = 0
		for j in range(8):
			res[7 - j] = res[7 - j] ^ xbin[7 - j]
	x = ""
	x += BinToHex(res[0:4])
	x += BinToHex(res[4:8])
	return x;

def MixColumn(mode, matrix):
	res = []
	for i in range(4):
		res.append([])
		for j in range(4):
			x = "00"
			for k in range(4):
				x = Xor(x, Mul(mode[i][k], matrix[k][j]))
			res[i].append(x)
	return res;