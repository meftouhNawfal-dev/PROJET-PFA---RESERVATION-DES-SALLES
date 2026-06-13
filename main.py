from View import login
from View import admin
from Model import model

def lancer_app():
    model.initialisation_bd()
    # login.login_fenetre()
    admin.admin_fenetre("admin")
    
if __name__  == "__main__":
    lancer_app()
    
