from Model import model

def authentifier(nom, mdp,label_erreur):
    label_erreur.config(text="")
    if not nom.strip() or not mdp.strip():
        label_erreur.config(text="Veuillez remplir tous les champs.")
        return
    
    utulisateur = model.get_utulisateur_nom(nom)
    
    if utulisateur is None:
        label_erreur.config(text="Le nom d'utulisateur est incorrect.")
        return
    
    if utulisateur["Password"].value[0] != mdp.strip():
        label_erreur.config(text="Le mot de passe d'utulisateur est incorrect.")        
        return
    
    
    
    