import json

FICHIER_JSON = "Utilisateurs.json"

def charger_utilisateurs():
    try:
        with open(FICHIER_JSON, "r") as fichier:
            data = json.load(fichier)
            return data["utilisateurs"]
    except FileNotFoundError:
        return [] 

def sauvegarder_utilisateurs(utilisateurs):
    with open(FICHIER_JSON, "w") as fichier:
        data = {"utilisateurs": utilisateurs}
        json.dump(data, fichier, indent=4)

def ajouter_utilisateur(utilisateurs):
    nom = input("Entrez le nom de l'utilisateur : ")
    prenom = input("Entrez votre prenom : ")
    email = input("Entrez l'email de l'utilisateur : ")
    age = int(input("Entrez l'âge de l'utilisateur : "))
    utilisateur = {"nom": nom, "prenom": prenom, "email": email, "age": age}
    utilisateurs.append(utilisateur)
    print(f"L'utilisateur {nom} a été ajouté avec succès.")


def afficher_utilisateurs(utilisateurs):
    if utilisateurs:
        for i, utilisateur in enumerate(utilisateurs, 1):
            print(f"{i}. Nom : {utilisateur['nom']}, Prenom : {utilisateur['prenom']}, Email : {utilisateur['email']}, Âge : {utilisateur['age']}")
    else:
        print("Aucun utilisateur n'a été ajouté.")

def connextion(utilisateurs):
    prenom = input("prenom :")
    nom = input("nom :")

    for utilisateur in utilisateurs:
        if utilisateur['prenom'] == prenom and utilisateur['nom'] == nom:
            print(f"Connextion validé pour {prenom}")
            return True
        print("Erreur de prenom et nom")
        return False
    


def menu():
    utilisateurs = charger_utilisateurs() 

    while True:
        print("\n--- Gestion des Utilisateurs ---")
        print("1. Ajouter un utilisateur")
        print("2. Afficher les utilisateurs")
        print("3. Se connecter")
        print("4. Quitter")
        choix = input("Choisir une option : ")

        if choix == "1":
            ajouter_utilisateur(utilisateurs)
            sauvegarder_utilisateurs(utilisateurs)  
        elif choix == "2":
            afficher_utilisateurs(utilisateurs)
        elif choix == "3":
            connextion(utilisateurs)
            if connextion(utilisateurs) == True:
                print("1. Voir mes cours")
                print("2. Voir les événements en lien avec mes cours")
        elif choix == "4":
            break
        else:
            print("Option invalide. Veuillez essayer à nouveau.")

if __name__ == "__main__":
    menu()
