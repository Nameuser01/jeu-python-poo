#!/usr/bin/python3
from random import randrange
def menu():
	message = "Affichage du menu"
	underscore = "_"
	print(underscore*len(message))
	print(message)
	print("'0' : Quitter le programme")
	print("'1' : Lancer une phase de combat")
	print("'2' : Afficher le gagant (si la partie est finie)")
	print("'3' : Afficher les informations d'un joueur")
	"""print("'4' : Changer les noms des joueurs")
	print("'5' : Changer le nombre de points de vie des joueurs")
	print("'6' : Changer le nombre de dégâts que peut faire un joueur (max value)")
	print("'8' : Lancer le combat jusqu'à ce qu'un joueur gagne")"""

def infos():
	print("---", user1.get_name(), "a", user1.get_hp(), "hp ---")
	print("---", user2.get_name(), "a", user2.get_hp(), "hp ---\n")

def player_infos(player_to_modifie):#Afficher les informations d'un personnage uniquement en fonction de la variable d'entrée
	if (player_to_modifie == 1):
		print("\nNom :",user1.get_name())
		print("Life :",user1.get_hp())
	elif(player_to_modifie == 2):
		print("\nNom :",user2.get_name())
		print("Life :", user2.get_hp())
	else:
		print("Debog message for ligne 28 : erreur dans la condition. Transition : $modif -> $player_to_modifie pose problème")

class Player:

	def __init__(self, name):
		assert isinstance (name, str) and len(name) > 0
		self.name = name
		self.hp = 30

	def get_hp(self):
		return self.hp

	def get_name(self):
		return self.name

	def damages(self):
		damage = randrange(10)
		self.hp -= damage
		if (self.hp <= 0):
			print("---", self.name, "vient de mourir ---")
			self.hp = 0
		else:
			print(self.name, "vient de se faire attaquer, il lui reste :", self.hp, "hp")


user1 = Player("mario")
user2 = Player("luigi")
infos()
i = 0
token = False
while (token == False):
	menu()
	print("Que voulez vous faire ?")
	choix = int(input("> "))
	print()
	if(choix == 0):
		print("Vous décidez de quitter le progamme. À plus.")
		token = True

	elif(choix == 1):
		print("Le joueur", user1.get_name(), "attaque", user2.get_name())
		print("")
		user2.damages()
		print("\nLe joueur", user2.get_name(), "attaque", user1.get_name())
		print("")
		user1.damages()
		i+=1
		if (user2.get_hp() <= 0):
			print(user1.get_name(), "à tué", user2.get_name())
			print("La partie aura duré :", i, "tours")
			token = True
		elif(user1.get_hp() <= 0):
			print(user2.get_name(), "à tué", user1.get_name())
			print("La partie aura duré :", i, "tours")
			token = True
		else:
			print("")
	elif(choix == 2):
		if(user1.get_hp() <= 0):
			print("Le joueur :", user2.get_hp(), "est le gagnant.")
		elif (user2.get_hp() <= 0):
			print("Le joueur :", user1.get_hp(), "est le gagnant.")
		else:
			print("Il n'y a pas encore de vainqeur.")

		if(user1.get_hp() < user2.get_hp()):
			print("Par contre, le joueur",user2.get_name(), "à plus de points de vie que",user1.get_name(), "(", user2.get_hp(), "hp contre", user1.get_hp(),"hp)")
		elif(user1.get_hp() == user2.get_hp()):
			print("Le combat n'a pas encore commencé, les deux joueurs sont à", user1.get_hp(), "hp")
		else:
			print("Par contre, le joueur",user1.get_name(), "à plus de points de vie que",user2.get_name(), "(", user1.get_hp(), "hp contre", user2.get_hp(),"hp)")

		print("\n")
	elif(choix == 3):
		modif = 0
		print("Quel joueur voulez vous consulter ?\n('1' ou '2')")
		modif = int(input("> "))
		while (modif != 1 and modif != 2):
			print("Le nombre que vous venez d'entrer n'est pas valide, veuillez réessayer")
			modif = int(input("Retapez le numéro du personnage que vous voulez consulter (soit '1' soit '2')\n> "))
		player_infos(modif)
		forward = input("Appuyez sur entrée pour continuer...")
	else:
		print("Fin prématurée du programme")
		token = True

stars = "*"
endl = "End of this program !"
size_endl = len(endl)
print(stars*size_endl)
print(endl)
print(stars*size_endl)