from Model import model
from View import admin
from View import professeur

def authentifier(nom, mdp,label_erreur,fenetre_login):
    label_erreur.config(text="")
    nom = nom.strip()
    mdp = mdp.strip()
    if not nom.strip() or not mdp.strip():
        label_erreur.config(text="Veuillez remplir tous les champs.")
        return
    
    utilisateur = model.get_utilisateur_nom(nom)
    
    if utilisateur is None:
        label_erreur.config(text="Le nom d'utilisateur est incorrect.")
        return
    
    if utilisateur["Password"].values[0] != mdp.strip():
        label_erreur.config(text="Le mot de passe d'utilisateur est incorrect.")        
        return
    
    if utilisateur["Role"].values[0] == "administrateur":
        fenetre_login.destroy()
        admin.admin_fenetre(nom)
    
    if utilisateur["Role"].values[0] == "professeur":
        fenetre_login.destroy()
        professeur.professeur_fenetre()
    
    
    
    
    