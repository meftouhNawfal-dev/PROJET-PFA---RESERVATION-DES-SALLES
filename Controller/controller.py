from Model import model

def authentifier(nom, mdp,label_erreur):
    label_erreur.config(text="")
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
    
    
    
    