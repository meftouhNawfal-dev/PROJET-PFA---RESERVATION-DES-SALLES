from Model import model
from View import admin
from View import professeur
import tkinter as tk
from tkinter import messagebox

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
        
def afficher_utilisateurs(tableau):
    for item in tableau.get_children():
        tableau.delete(item)
    
    liste_utilisateurs= model.get_liste_utilisateur()
    
    for utilisateur in liste_utilisateurs:
        tableau.insert("", "end", values=(utilisateur["ID_Utilisateur"],utilisateur["Nom_Utilisateur"],utilisateur["Role"],utilisateur["Password"])) #tuple(utilisateur.values()
    

def creer_utilisateur(nom,pswd,role):
    root = tk.Tk()
    root.destroy()
    
    if not nom.strip() or not pswd.strip() or not role.strip():
        messagebox.showerror( "Erreur", "Veuillez remplir tous les champs.")
        return
    
    resultat = model.ajouter_utilisateur(nom,pswd,role)
    if resultat == False:
        messagebox.showerror( "Erreur", f"Le nom d'utilisateur '{nom}' existe déjà.")
        return
    else:
        messagebox.showinfo("Succès", f"Utilisateur '{nom}' créé avec succès.")

    