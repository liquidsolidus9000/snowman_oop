from random import choice, randint, seed


class Snowman:
	allowed_colors = ["red","green","orange","checker","white","black","indigo","turquoise","violet","maroon","yellow"]
	def __init__(self,name, snowman_id=0):
		seed(snowman_id)
		self.name = name
		self.hat= choice(Snowman.allowed_colors)
		self.scarf = choice(Snowman.allowed_colors)
		self.buttons = randint(0,5)
		self.balls = randint(1,4)

	def __repr__(self):
		hat_article = "a"
		scarf_article = "a"
		if self.hat[0] in "aeiou":
			hat_article = "an"
		if self.scarf[0] in "aeiou":
			scarf_article = "an"
		return f"{self.name} is wearing {hat_article} {self.hat} hat, {scarf_article} {self.scarf} scarf, {self.buttons} buttons, and consists of {self.balls} balls."

frosty =  Snowman("Frosty",0)
olaf = Snowman("Olaf",1)
frostys_brother = Snowman("Frosty's brother",3)


snowmen = [Snowman(f"Snowman {i}",i) for i in range(4,20)]

print(frosty)
print(olaf)
print(frostys_brother)
for s in snowmen:
	print(s)


# def dressup(self):


		# self.hat = hat
		# self.scarf = scarf
		# self.buttons = buttons
		# self.balls = balls