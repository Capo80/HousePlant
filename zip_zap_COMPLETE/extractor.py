from subprocess import Popen, PIPE, STDOUT, call
from pwn import *

fd = open ("xato-net-10-million-passwords-100.txt", "r")
passwords = fd.readlines()

def filetype(filename):
	p = Popen(['file', filename], stdout=PIPE, stdin=PIPE, stderr=STDOUT)  
	out = p.communicate()[0]
	if ("Zip" in out.decode().strip()):
		return "zip"
	elif ("POSIX tar archive" in out.decode().strip()):
		return "tar"
	elif ("gzip compressed" in out.decode().strip()):
		return "gzip"
	else:
		return "zip"
		exit()

def break_zip(filename):
	p = process("/snap/bin/john-the-ripper.zip2john "+filename+" > zip.hashes", shell=True)
	p = process("john zip.hashes -w=xato-net-10-million-passwords-100.txt", shell=True)
	for i in range(0, 4):
		recv = p.recvline()
	recv = p.recvline()
	passwd = recv.split(b" ")[0].strip()
		
	print(passwd)

	p = call(['unzip', "-P", str(passwd)[2:-1],  filename, "-d", "extr_dir"])
	p = call(['rm', filename])
	p = call(['rm', "/home/cc20-sapienza/snap/john-the-ripper/297/.john/john.pot"])


p = Popen(['rm', "/home/cc20-sapienza/snap/john-the-ripper/297/.john/john.pot"])
while True:

	p = Popen(['ls', "extr_dir"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)  
	out = p.communicate()[0]
		
	res = filetype("extr_dir/" + str(out)[2:-3])
	
	print("extr_dir/"+str(out)[2:-3])
	if (res == "gzip"):
		if ("." not in str(out)[2:-3]):
			p = call(['mv', "extr_dir/" + str(out)[2:-3], "extr_dir/" + str(out)[2:-3]+ ".gz"]) 
			p = call(['gunzip', "extr_dir/" + str(out)[2:-3] + ".gz"])
			
		else:
			p = call(['gunzip', "extr_dir/" + str(out)[2:-3]]) 
	elif (res == "tar"):
		p = call(['tar', '-xf', "extr_dir/"+str(out)[2:-3], "-C", "extr_dir"])
		p = call(['rm', "extr_dir/" + str(out)[2:-3]])
	elif (res == "zip"):
		break_zip("extr_dir/"+str(out)[2:-3])
		
	




# p = Popen(['grep', 'f'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
# grep_stdout = p.communicate(input=b'one\ntwo\nthree\nfour\nfive\nsix\n')[0]
# print(grep_stdout.decode())