import webbrowser

# Définition des options
options = {
    "1": {"plateforme": "Facebook", "lien": "https://www.facebook.com/jaylan.lking"},
    "2": {"plateforme": "WhatsApp", "numero": "+261385181817"},
    "3": {"plateforme": "Télégramme", "lien": "https://t.me/+Ktzwc92-AuEyYmQ0"}
}

# Affichage des options
print("Options:")
for key, value in options.items():
    print(key + ". " + value["plateforme"])

# Demande à l'utilisateur de choisir une option
choix = input("Entrez votre choix (1, 2 ou 3): ")

# Vérification du choix de l'utilisateur
if choix in options:
    if choix == "1":
        # Ouvre le lien vers Facebook
        webbrowser.open(options[choix]["lien"])
        print("Vous avez choisi d'envoyer un message sur Facebook.")
    elif choix == "2":
        # Ouvre directement le numéro WhatsApp
        print("Vous avez choisi d'envoyer un message sur WhatsApp. Voici le message : Salut ividy 2toi 500ar za de 1000ar no alefanao amikou.")
        print("Vous pouvez me contacter au numéro:", options[choix]["numero"])
    else:
        # Ouvre le lien d'invitation pour Telegram
        webbrowser.open(options[choix]["lien"])
        print("Vous avez choisi d'envoyer un message sur Télégramme. Lorsque vous rejoignez le groupe, vous recevrez un message automatique de bienvenue.")
else:
    print("Choix invalide.")