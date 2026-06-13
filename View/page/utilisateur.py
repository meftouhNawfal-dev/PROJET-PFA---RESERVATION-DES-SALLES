import tkinter as tk
from View.ui_theme import *
from tkinter import ttk
from Controller import controller

def creer_page_utilisateur(zone_contenu):

    page = tk.Frame(zone_contenu, bg=C_CONTENU)

    tk.Label(
        page,
        text="GESTION DES UTILISATEURS",
        font=("Arial", 13, "bold"),
        bg=C_CONTENU,
        fg=C_TEXTE_TITRE
    ).pack(pady=20, padx=20, anchor="w")

    input_fram = tk.Frame(page, bg="white")
    input_fram.pack(fill="x", padx=20, pady=(5, 20))

    # Titre du formulaire
    tk.Label(
        input_fram,
        text="Créer un nouvel utilisateur",
        font=("Arial", 12, "bold"),
        bg="white",
        fg=C_TEXTE_TITRE
    ).grid(
        row=0,
        column=0,
        columnspan=5,
        sticky="w",
        padx=20,
        pady=20
    )
    
    def vider_champs(input_nom, input_psw, menu_role):
        input_nom.delete(0, tk.END)
        input_psw.delete(0, tk.END)
        menu_role.set("")
        
    def creer_vider_utilisateur():
        controller.creer_utilisateur(
            input_nom.get(),
            input_psw.get(),
            menu_role.get(),
        )
        controller.afficher_utilisateurs(tableau)
        vider_champs(input_nom, input_psw, menu_role)
    
    btn_creer = tk.Button(
        input_fram,
        text="Créer un utilisateur",
        font=("Arial", 11, "bold"),
        bg=C_VERT,
        fg="white",
        bd=1,
        relief="solid",
        cursor="hand2",
        activebackground=C_VERT_HOVER,
        activeforeground="white",
        padx=7,
        command= creer_vider_utilisateur
    )
    btn_creer.grid(
        row=0,
        column=5,
        sticky="e",
        padx=20,
        pady=20
    )

    # Nom utilisateur
    tk.Label(
        input_fram,
        text="Nom utilisateur :",
        font=("Arial", 11),
        bg="white",
        fg=C_TEXTE_TITRE
    ).grid(
        row=1,
        column=0,
        sticky="w",
        padx=(20, 10),
        pady=10
    )

    input_nom = tk.Entry(
        input_fram,
        font=("Arial", 11),
        width=25,
        bd=1,
        relief="solid"
    )
    input_nom.grid(
        row=1,
        column=1,
        padx=(0, 20),
        pady=10
    )

    # Mot de passe
    tk.Label(
        input_fram,
        text="Mot de passe :",
        font=("Arial", 11),
        bg="white",
        fg=C_TEXTE_TITRE
    ).grid(
        row=1,
        column=2,
        sticky="w",
        padx=(0, 10),
        pady=10
    )

    input_psw = tk.Entry(
        input_fram,
        font=("Arial", 11),
        width=25,
        bd=1,
        relief="solid",
    )
    input_psw.grid(
        row=1,
        column=3,
        padx=(0, 20),
        pady=10
    )
    
    # Role
    tk.Label(
        input_fram,
        text="Role :",
        font=("Arial", 11),
        bg="white",
        fg=C_TEXTE_TITRE
    ).grid(
        row=1,
        column=4,
        sticky="w",
        padx=(0, 10),
        pady=10
    )
    
    menu_role = ttk.Combobox(
        input_fram,
        font=("Arial", 11),
        values=["Administrateur","Professeur"],
        state="readonly",
        width=20
    )
    menu_role.grid(
        row=1,
        column=5,
        sticky="w",
        padx=(0, 10),
        pady=10
    )

    tableau_frame = tk.Frame(page, bg="white")
    tableau_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
    
    # ==================== TITRE TABLEAU ====================

    tk.Label(
        tableau_frame,
        text="Liste des utilisateurs",
        font=("Arial", 12, "bold"),
        bg="white",
        fg=C_TEXTE_TITRE
    ).pack(anchor="w", padx=20, pady=(20, 10))


    # ==================== BARRE D'ACTION ====================

    action_frame = tk.Frame(tableau_frame, bg="white")
    action_frame.pack(fill="x", padx=20, pady=(0, 15))

    btn_modifier = tk.Button(
        action_frame,
        text="Modifier",
        font=("Arial", 10, "bold"),
        bg = C_ORANGE,
        fg="white",
        cursor="hand2",
        padx=10
    )
    btn_modifier.pack(side="left", padx=(0, 10))

    btn_supprimer = tk.Button(
        action_frame,
        text="Supprimer",
        font=("Arial", 10, "bold"),
        bg=C_ROUGE,
        fg="white",
        cursor="hand2",
        padx=10
    )
    btn_supprimer.pack(side="left")

    # Zone recherche
    recherche_frame = tk.Frame(action_frame, bg="white")
    recherche_frame.pack(side="right")

    tk.Label(
        recherche_frame,
        text="Recherche :",
        bg="white",
        font=("Arial", 10)
    ).pack(side="left", padx=(0, 5))

    entree_recherche = tk.Entry(
        recherche_frame,
        font=("Arial", 10),
        width=25
    )
    entree_recherche.pack(side="left", padx=(0, 5))

    btn_rechercher = tk.Button(
        recherche_frame,
        text="Rechercher",
        font=("Arial", 10),
        bg=C_BLEU,
        fg="white",
        cursor="hand2"
    )
    btn_rechercher.pack(side="left")


    # ==================== TABLEAU ====================

    

    tableau = ttk.Treeview(
        tableau_frame,
        columns=("id","nom","role","motdepasse"),
        show="headings",
        height=10
    )

    tableau.heading("id", text="ID")
    tableau.heading("nom", text="Nom d'utilisateur")
    tableau.heading("role", text="Rôle")
    tableau.heading("motdepasse", text="Mot de passe")

    tableau.column("id", width=80, anchor="center")
    tableau.column("nom", width=250,anchor= "center")
    tableau.column("role", width=180, anchor="center")
    tableau.column("motdepasse", width=200)

    # Données de test
    # tableau.insert("", "end", values=(1, "admin", "Administrateur", "1234"))
    # tableau.insert("", "end", values=(2, "prof1", "Professeur", "abcd"))

    # Scrollbar
    scroll = ttk.Scrollbar(
        tableau_frame,
        orient="vertical",
        command=tableau.yview
    )

    tableau.configure(yscrollcommand=scroll.set)

    tableau.pack(side="left", fill="both", expand=True, padx=(20, 0), pady=(0, 20))
    scroll.pack(side="right", fill="y", pady=(0, 20))
    
    
    controller.afficher_utilisateurs(tableau)
    
    
    return page