alphabet = {				#dictionary maps letter : numbers
 "a" : 1,
 "b" : 2,
 "c" : 3,
 "d" : 4,
 "e" : 5,
 "f" : 6,
 "g" : 7,
 "h" : 8,
 "i" : 9,
 "j" : 10,
 "k" : 11,
 "l" : 12,
 "m" : 13,
 "n" : 14,
 "o" : 15,
 "p" : 16,
 "q" : 17,
 "r" : 18,
 "s" : 19,
 "t" : 20,
 "u" : 21,
 "v" : 22,
 "w" : 23,
 "x" : 24,
 "y" : 25,
 "z" : 26,
 " " : " ",
 "." : ".",
 "," : ",",
 "!" : "!",
 ":" : ":"
 }
inv_alphabet = {v: k for k, v in alphabet.items()}		#reverses the mapping

def a1z26(code_input):		#translates letters into numbers
	splitinput = list(code_input)
	for i in splitinput:
		outputnum.append(alphabet[i])
	print outputnum
def inva1z26(code_input): 	#reverses numbers into letters
	split_code = code_input.split(",")
	for i in split_code:
		try:									#this allows to include space in the code
			i = int(i)
			outputlet.append(inv_alphabet[i])
		except:
			outputlet.append(inv_alphabet[i])
	print outputlet
def rotn(code_input):		#shifts the alphabet
	rotmod = int(raw_input("Enter by how much you want to shift the alphabet: ")) 
	splitinput = list(code_input)
	for i in splitinput:
		try:
			modindex = alphabet[i] + rotmod
			if modindex > 26:
				modindex = modindex - 26
			elif modindex <= 0:
				modindex = 26 + modindex
			outputnum.append(modindex)
		except:
			outputnum.append(i)
	
	for i in outputnum:
		outputlet.append(inv_alphabet[i])
	print outputlet
def derotn(code_input):		#reverses the shift
	rotmod = int(raw_input("Enter by how much was the code shifted: "))
	splitinput = list(code_input)
	for i in splitinput:
		try:
			modindex = alphabet[i] - rotmod
			if modindex > 26:
				modindex = modindex - 26
			elif modindex <= 0:
				modindex = 26 + modindex
			outputnum.append(modindex)
		except:
			outputnum.append(i)
	
	for i in outputnum:
		outputlet.append(inv_alphabet[i])
	print outputlet

code_lib = {				#allows to choose which code you'd like to use from terminal
	"a1z26" : a1z26,
	"inva1z26" : inva1z26,
	"rotn" : rotn,
	"derotn" : derotn
	}
outputnum = []
outputlet = []

code_input = raw_input("Enter your code here: ")
code_choice = raw_input("Enter which code you'd like to use: ")
if code_choice in code_lib:
	code_lib[code_choice](code_input)
else:
	print "Code not found"

