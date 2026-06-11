import tkinter as tk
from View.ui_theme import *

def creer_page_reservation(zone_contenu):

        page = tk.Frame(zone_contenu, bg=C_CONTENU)

        tk.Label(
            page,
            text="GESTION DES RESERVATIONS",
            font=("Arial", 24, "bold"),
            bg=C_CONTENU,
            fg=C_TEXTE_TITRE
        ).pack(pady=30)

        return page