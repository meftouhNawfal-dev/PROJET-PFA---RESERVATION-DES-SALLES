import tkinter as tk
from View.ui_theme import *
from View import login
from View.page import utilisateur
from View.page import reservations
from View.page import tableau_de_bord
from View.page import salles
from View.page import seances


def admin_fenetre(nomAdmin):

    fenetre = tk.Tk()
    fenetre.title("Page Admin")
    fenetre.geometry("400x350+400+100")
    fenetre.state("zoomed")

    # ================= TOPBAR =================

    topBar = tk.Frame(fenetre, bg=C_TOPBAR, height=56)
    topBar.pack(fill="x", side="top")
    topBar.pack_propagate(False)

    def deconnecter():
        fenetre.destroy()
        login.login_fenetre()

    tk.Label(
        topBar,
        text="Gestion Des Salles",
        font=("Arial", 18, "bold"),
        bg=C_TOPBAR,
        fg=C_TEXTE_TITRE
    ).pack(side="left", padx=20)

    tk.Button(
        topBar,
        text="Déconnexion",
        font=("Arial", 11),
        bd=1,
        relief="solid",
        bg="#ebebeb",
        command=deconnecter
    ).pack(side="right", padx=20)

    tk.Label(
        topBar,
        text=nomAdmin,
        font=("Arial", 12, "bold"),
        bg=C_TOPBAR,
        fg=C_TEXTE_TITRE
    ).pack(side="right", padx=5)

    # ================= CORPS =================

    corps = tk.Frame(fenetre, bg=C_FOND_APP)
    corps.pack(fill="both", expand=True)

    # ================= SIDEBAR =================

    sidebar = tk.Frame(corps, bg=C_SIDEBAR, width=220)
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)

    tk.Label(
        sidebar,
        text="NAVIGATION",
        font=("Arial", 11, "bold"),
        fg=C_TEXTE_DISCRET,
        bg=C_SIDEBAR
    ).pack(anchor="w", padx=20, pady=(20, 15))
    
    menu_frame = tk.Frame(sidebar,bg=C_SIDEBAR)
    menu_frame.pack(fill="x", padx=5, pady=(5, 10))

    # ================= CONTENU =================

    zone_contenu = tk.Frame(corps, bg=C_CONTENU)
    zone_contenu.pack(fill="both", expand=True)

    # ================= PAGES =================

    pages = {
        "Tableau de bord" : tableau_de_bord.creer_page_tableDeBord(zone_contenu),
        "Salles" : salles.creer_page_salle(zone_contenu),
        "Séances" : seances.creer_page_seance(zone_contenu),
        "Utilisateurs" : utilisateur.creer_page_utilisateur(zone_contenu),
        "Réservations" : reservations.creer_page_reservation(zone_contenu)
    }

    # ================= MENU =================

    def afficher_page(nom):

        for page in pages.values():
            page.pack_forget()

        pages[nom].pack(fill="both", expand=True)

       
    def creer_bouton_menu(texte, icone):

        btn = tk.Button(
            menu_frame,
            text=f"{icone}   {texte}",
            font=("Arial", 11),
            bg=C_SIDEBAR_HOVER,
            fg=C_TEXTE_SIDEBAR,
            bd=0,
            relief="flat",
            anchor="w",
            padx=15,
            pady=10,
            cursor="hand2",
            activebackground=C_SIDEBAR_HOVER,
            activeforeground="white",
            command=lambda: afficher_page(texte)
        )

        btn.pack(fill="x",padx=8,pady=4)

    # ================= BOUTONS =================

    creer_bouton_menu("Tableau de bord", "📊")
    creer_bouton_menu("Salles", "🏢")
    creer_bouton_menu("Séances", "🕒")
    creer_bouton_menu("Utilisateurs", "👥")
    creer_bouton_menu("Réservations", "📋")

    # ================= PAGE PAR DEFAUT =================

    afficher_page("Utilisateurs")
    fenetre.mainloop()