import tkinter as tk
from View.ui_theme import *


def professeur_fenetre():
    fenetre = tk.Tk()
    fenetre.title("Page professeur")
    fenetre.geometry("400x350+500+140")
    fenetre.state("zoomed")
    
    tk.Label(text="Page professeur",font=("Arial",20,"bold"),fg=C_TEXTE_TITRE).pack(pady=(30,25))
    
    fenetre.mainloop()