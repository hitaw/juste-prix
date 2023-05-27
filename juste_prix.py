import random

jeu = True
while jeu:
	
	random.seed()

	print("\nBienvenue dans le Juste Prix ! \nDans ce jeu, vous allez devoir deviner le numéro choisi par l'ordinateur, bonne chance !")

	est_int = False

	while not est_int:

		borne = input("\nVeuillez entrer la borne maximum (nombre entier) : ")

		est_int = True
		for c in borne:
			if c < '0' or c > '9':
				est_int = False
				print("\nCe n'est pas un nombre entier.")
				break

	borne = int(borne)
	nombre = random.randint(0, borne)

	choix = -1
	essai = 0

	print("Le jeu commence !\n")
	while choix != nombre:
		essai += 1
		
		est_int = False

		while not est_int:

			choix = input("\nVeuillez entrer un nombre entier : ")

			est_int = True
			for c in choix:
				if c < '0' or c > '9':
					est_int = False
					print("\nCe n'est pas un nombre entier.")
					break

		choix = int(choix)

		if choix < nombre:
			print("\nC'est plus !")
		elif choix > nombre:
			print("\nC'est moins !")
		else:
			print ("Bravo ! Vous avez trouvé en ", essai, " essais !")

	reponse = input("Recommencer ? (Oui/Non) ")
	reponse = reponse.lower()
	jeu = reponse == 'oui'

