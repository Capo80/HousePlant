stringa = "....- ..... ...-. .--.- .--.. ....- -..-- -..-. ..--. -.... .-... .-.-. .-.-. ..-.. ...-- ..... .--.. ...-- .-.-- .--.- -.... -...- .-... ..-.- .-... ..-.. ...--"

for i in stringa:
	if i == " ":
		print(" ", end='')
	elif (i == "."):
		print("1", end='')
	elif (i == "-"):
		print("0", end='')
print("")