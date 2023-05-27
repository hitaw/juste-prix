import random 

random.seed()

jeu = True

while jeu:
	print("\nBienvenue dans le juste prix version ordinateur !\nChoisissez un nombre et l'ordinateur devra trouver grâce à vos indications !")

	est_int = False

	while not est_int:

		borne_sup_init = input("\nVeuillez entrer la borne maximum (nombre entier) : ")

		est_int = True
		for c in borne_sup_init:
			if c < '0' or c > '9':
				est_int = False
				print("\nCe n'est pas un nombre entier.")
				break

	borne_sup = int(borne_sup_init)
	borne_inf = 0

	essai = 0
	reponse = ""

	while reponse.lower() != "trouvé":

		essai += 1

		choix = random.randint(borne_inf, borne_sup)

		print("\nL'ordinateur a choisi : ", choix)

		est_option = False
		option = ["plus","moins","trouvé"]

		while not est_option:
			reponse = input("\nIndication (Plus/Moins/Trouvé) : ")

			if reponse.lower() not in option:
				print("\nEntrée Invalide.")
			else:
				est_option = True

		if reponse.lower() == "plus":
				borne_inf = choix + 1
		elif reponse.lower() == "moins":
				borne_sup = choix - 1

		if borne_inf > borne_sup:
			print("Ahah très drôle, il ne faut pas mentir!")
			borne_inf = 0
			borne_sup = int(borne_sup_init)


	print("La réponse est : ", choix, "\nTrouvée en ", essai, " essais.")

	continuer = input("Recommencer ? (Oui/Non) ")
	continuer = continuer.lower()
	jeu = continuer == 'oui'