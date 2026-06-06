import tkinter as tk
from View.ui_theme import *
from Controller import controller

def login_fenetre():
    fenetre = tk.Tk()
    fenetre.title("Connexion")
    fenetre.geometry("400x350+500+140")
    fenetre.resizable(False,False)
    
    tk.Label(text="Connexion",font=("Arial",20,"bold"),fg=C_TEXTE_TITRE).pack(pady=(30,25))
    
    tk.Label(text="Nom d'utilisateur",font=("Arial",11),fg=C_TEXTE_TITRE).pack()
    
    champ_nom = tk.Entry(fenetre, font=("Arial",11), width = 30, relief="solid" )
    champ_nom.pack(pady=(5,30), ipady=6)
    
    tk.Label(text="Mot de passe",font=("Arial",11),fg=C_TEXTE_TITRE).pack()
    
    champ_psd = tk.Entry(fenetre, font=("Arial",11), width = 30, relief="solid",show="*" )
    champ_psd.pack(pady=(5,10), ipady=6)
    
    label_erreur = tk.Label(fenetre,text="",font=("Arial",11),fg=C_ROUGE)
    label_erreur.pack(pady=5)
    
    tk.Button(fenetre, text="Se connecter", width= 20, font=("Arial",11),bg= C_BLEU,
              command=lambda: controller.authentifier(champ_nom.get(),champ_psd.get(),label_erreur, fenetre)).pack()
    
    fenetre.bind("<Return>",lambda e: controller.authentifier(champ_nom.get(),champ_psd.get(),label_erreur, fenetre))
    
    
    fenetre.mainloop()