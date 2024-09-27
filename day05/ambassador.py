invites = ["Alice", "Géraldine", "Ivan", "Paul"];
queue = [
    "Alice", "Bob", "Clara", "David", "Eva", "Félix", "Gabrielle", "Hugo", "Isabelle", "Jean",
    "Katherine", "Louis", "Marie", "Nicolas", "Olivia", "Paul", "Quentin", "Rosa", "Simon", "Thérèse",
    "Ursule", "Victor", "Wendy", "Xavier", "Yasmine", "Zacharie", "Anaïs", "Bastien", "Chloé", "Dylan",
    "Élodie", "Florian", "Géraldine", "Hélène", "Ivan", "Jade", "Kevin", "Léa", "Mathieu", "Nina",
    "Olivier", "Pascale", "Romain", "Sophie", "Thomas", "Ulysses", "Véronique", "William", "Xena", "Yannick",
    "Zoé", "Amandine", "Benoît", "Céline", "Denis", "Estelle"
];

for people in queue :
	if people in invites :
		print("Welcome in\n");
	else :
		print("Get lost !\n");
		
