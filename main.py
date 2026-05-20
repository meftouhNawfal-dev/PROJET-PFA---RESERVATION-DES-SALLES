from View import login
from Model import model

def lancer_app():
    model.initialisation_bd()
    login.login_fenetre()
    
if __name__  == "__main__":
    lancer_app()
    
