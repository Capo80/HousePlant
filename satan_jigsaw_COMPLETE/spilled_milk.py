from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse
from PIL import Image, ImageDraw

img = Image.new('RGB', (300, 300), color = 'red')
pix_fin = img.load()

fd = open("out.txt", "r")
lines = fd.readlines()

for i in range(0, 10):
	im = Image.open("chall/"+lines[i].strip()) # Can be many different formats.
	pix = im.load()
	print(pix[0,0])

for i in range(0, len(lines)):
	curr = lines[i].split(".")[0]
	curr = str(long_to_bytes(int(curr)))[2:-1].split(" ")
	curr[0] = int(curr[0])
	curr[1] = int(curr[1])
	print(curr, " ",  lines[i])
	im = Image.open("chall/"+lines[i].strip()) # Can be many different formats.
	pix = im.load()
	pix_fin[curr[0], curr[1]] = pix[0,0]

img.save("final.jpg")

# for i in range(10000, 10100):
# 	print(lines[i])