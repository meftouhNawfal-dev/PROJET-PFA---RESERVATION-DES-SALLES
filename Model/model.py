import pandas as pd
import os 


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
