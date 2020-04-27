lista = ["(doorbell rings)",
"delphine: Jess, I heard you've been stressed, you should know I'm always ready to help!",
"Jess: Did you make something? I'm hungry...",
"Delphine: Of course! Fresh from the bakery, I wanted to give you something, after all, you do so much to help me all the time!",
"Jess: Aww, thank you, Delphine! Wow, this bread smells good. How is the bakery?",
"Delphine: Lots of customers and positive reviews, all thanks to the mention in rtcp!",
"Jess: I am really glad it's going well! During the weekend, I will go see you guys. You know how much I really love your amazing black forest cakes.",
"Delphine: Well, you know that you can get a free slice anytime you want.",
"(doorbell rings again)s",
"Jess: Oh, that must be Vihan, we're discussing some important details for rtcp.",
"Delphine: sounds good, I need to get back to the bakery!",
"Jess: Thank you for the bread! <3"]

lista = """(doorbell rings)
delphine: Jess, I heard you've been stressed, you should know I'm always ready to help!
Jess: Did you make something? I'm hungry...
Delphine: Of course! Fresh from the bakery, I wanted to give you something, after all, you do so much to help me all the time!
Jess: Aww, thank you, Delphine! Wow, this bread smells good. How is the bakery?
Delphine: Lots of customers and positive reviews, all thanks to the mention in rtcp!
Jess: I am really glad it's going well! During the weekend, I will go see you guys. You know how much I really love your amazing black forest cakes.
Delphine: Well, you know that you can get a free slice anytime you want.
(doorbell rings again)
Jess: Oh, that must be Vihan, we're discussing some important details for rtcp.
Delphine: sounds good, I need to get back to the bakery!
Jess: Thank you for the bread! <3"""

lista = ["(doorbell rings)",
"delphine: Jess, I heard you've been stressed, you should know I'm always ready to help!",
"Jess: Did you make something? I'm hungry...",
"Delphine: Of course! Fresh from the bakery, I wanted to give you something, after all, you do so much to help me all the time!",
"Jess: Aww, thank you, Delphine! Wow, this bread smells good. How is the bakery?",
"Delphine: Lots of customers and positive reviews, all thanks to the mention in rtcp!",
"Jess: I am really glad it's going well! During the weekend, I will go see you guys. You know how much I really love your amazing black forest cakes.",
"Delphine: Well, you know that you can get a free slice anytime you want.",
"(doorbell rings again)s",
"Jess: Oh, that must be Vihan, we're discussing some important details for rtcp.",
"Delphine: sounds good, I need to get back to the bakery!",
"Jess: Thank you for the bread! <3"]

for j in range(0, 20):	
	print(j, ": ", end = '')
	for i in lista:
		print(i[j], end='')
	print("")

