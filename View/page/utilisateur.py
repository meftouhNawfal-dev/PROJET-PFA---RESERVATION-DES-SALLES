import tkinter as tk
from View.ui_theme import *
from tkinter import ttk

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
        padx=7  
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
    input_fram.pack(fill="x", padx=20, pady=(5, 20))
    
    

    return page