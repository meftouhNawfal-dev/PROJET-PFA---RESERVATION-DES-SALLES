import pandas as pd
import os 
import tkinter as tk
from tkinter import messagebox


FICHIER_EXCEL = "DATA.xlsx"

FEUILLE_UTILISATEUR = "UTILISATEUR"
FEUILLE_SALLE = "SALLE"
FEUILLE_RESERVATION = "RESERVATION"
FEUILLE_SEANCE = "SEANCE"


def initialisation_bd():
    if os.path.exists(FICHIER_EXCEL):
        return
    
    table_utilisateur = pd.DataFrame([{"ID_Utilisateur":1,"Nom_Utilisateur":"admin","Password":"123","Role":"administrateur"},
           {"ID_Utilisateur":2,"Nom_Utilisateur":"prof","Password":"123","Role":"professeur"}                           
                                      ])
    table_salle = pd.DataFrame(columns=["ID_Salle","Nom_Salle","Capacite"])
    table_reservation = pd.DataFrame(columns=["ID_Reservation","Date_Reservation","ID_Utilisateur","ID_Salle"])
    table_seance = pd.DataFrame(columns=["ID_Seance","Heure_Debut","Heure_Fin"])
    
    writer = pd.ExcelWriter(FICHIER_EXCEL, engine="openpyxl")
    table_utilisateur.to_excel(writer,sheet_name=FEUILLE_UTILISATEUR, index= False)
    table_salle.to_excel(writer,sheet_name=FEUILLE_SALLE, index= False)
    table_reservation.to_excel(writer,sheet_name=FEUILLE_RESERVATION, index= False)
    table_seance.to_excel(writer,sheet_name=FEUILLE_SEANCE, index= False)
    writer.close()

def lire_feuille(nom_feuille):
    try:
        df = pd.read_excel(FICHIER_EXCEL, sheet_name= nom_feuille, dtype=str )
    except:
        df = pd.DataFrame()
    return df
        
def get_utilisateur_nom(nom_utilisateur):
    df = lire_feuille(FEUILLE_UTILISATEUR)
    if df.empty:
        root = tk.Tk()
        root.destroy()
        messagebox.showerror("Erreur","La BD est vide")
        return None
    resultat = df[df["Nom_Utilisateur"].str.lower() == nom_utilisateur.lower()]
    if resultat.empty:
        return None
    return resultat
        
        
def get_liste_utilisateur():
    df = lire_feuille(FEUILLE_UTILISATEUR)
    liste_utilisateur = df.to_dict("records")
    return liste_utilisateur

def sauvegarder_feuille(nom_feuille,df):
    with pd.ExcelWriter(FICHIER_EXCEL,engine="openpyxl",mode='a',if_sheet_exists="replace") as writer:
        df.to_excel(writer, sheet_name = nom_feuille, index = False)
    


def ajouter_utilisateur(nom,pswd,role):
    df = lire_feuille(FEUILLE_UTILISATEUR)
    
    if nom.strip().lower() in df["Nom_Utilisateur"].str.lower().values:
        return False
    
    if df.empty :
        id_user = 1
    else:
        id_user = int(df["ID_Utilisateur"].max()) + 1
    
    nouvel_utilisateur = pd.DataFrame(
        [
            {
                "ID_Utilisateur": id_user,
                "Nom_Utilisateur": nom.strip(),
                "Password": pswd.strip(),
                "Role": role.strip()
            }
        ]
    )
    
    new_df = pd.concat([df,nouvel_utilisateur],ignore_index=True)
    sauvegarder_feuille(FEUILLE_UTILISATEUR,new_df)
    return True
    
    
    