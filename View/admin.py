import tkinter as tk
from View.ui_theme import *
from View import login

def admin_fenetre(nom_utilisateur):
    fenetre = tk.Tk()
    fenetre.title("Page admin")
    fenetre.geometry("400x350+500+140")
    fenetre.state("zoomed")
    
    topBar = tk.Frame(fenetre,bg=C_TOPBAR, height=56)
    topBar.pack(fill="x")
    topBar.pack_propagate(False)
    
    def deconnecter():
        fenetre.destroy()
        login.login_fenetre()
    
    tk.Label(topBar,text="Gestion des salles",font=("Arial",18,"bold"),bg=C_TOPBAR,fg=C_TEXTE_TITRE).pack(side="left",padx=20)
    tk.Button(topBar,text="Deconnexion",font=("Arial",11),bg="red",bd=1,relief="solid",fg=C_CARTE,command=deconnecter).pack(side="right",padx=20)
    tk.Label(topBar,text=nom_utilisateur,font=("Arial",11,"bold"),bg=C_TOPBAR,fg=C_TEXTE_TITRE).pack(side="right",padx=5)
    
    corps = tk.Frame(fenetre,bg="green")
    corps.pack(fill="both",expand=True)
    
    sideBar = tk.Frame(corps,bg=C_SIDEBAR, width=210)
    sideBar.pack(fill="y",side="left")
    sideBar.pack_propagate(False)
    
    zoneContenu = tk.Frame(corps,bg=C_CONTENU)
    zoneContenu.pack(fill="both",expand=True)
    
    
    # tk.Label(text="Page admin",font=("Arial",20,"bold"),fg=C_TEXTE_TITRE).pack(pady=(30,25))
    
    fenetre.mainloop()