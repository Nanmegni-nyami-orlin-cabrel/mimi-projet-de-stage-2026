from datetime import datetime
import json

class Tache:
    def __init__(self,titre,description,statut,date_creation):
        self.titre = titre
        self.description = description
        self.statut="en cours"
        self.date_creation = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    def terminer(self):
        self.statut="terminer"
    def afficher(self):
        print(self.titre, "ayant pour description",self.description, "avec le statut",self.statut, "cree le ", self.date_creation)
class Gestionnaire:
    def __init__(self):
        self.listes_taches = []
    def ajouter_tache(self, titre, description):
        self.titre = titre
        self.description = description
        tache=Tache(titre,description)
        self.listes_taches.append(tache)
    def terminer(self, titre):
        self.titre = titre
        pass
    def supprimer_tache(self, titre):
        tache=Tache(titre)
        self.titre = titre
        self.listes_taches.remove(tache)
    def afficher_toutes(self):
        for tache in self.listes_taches:
            print("titre", self.titre, "statut", self.statut)
    def afficher_en_cours(self):
        for tache in self.listes_taches:
            if self.statut=="en cours":
                print("titre", self.titre, "statut", self.statut)
def sauvegarder():
    data=[]
    for tache in self.listes_taches:
        data.append(tache.__dict__)
    with open("taches.json", "w") as f:
        json.dump(data, f)



if __name__ == "__main__":

    gest=Gestionnaire()
    gest.ajouter_tache("laver_les_habits","larver avec de l'eau et du savon en frottant bien")
    gest.ajouter_tache("laverle sol", "larver le salon, la cuisine,et surtout la douche")
    gest.ajouter_tache("larver les assiettes", "larver les plats, les verres et les fourchettes")

    gest.terminer("laver les habits")
    gest.supprimer_tache("laver les habits")
    gest.afficher_toutes()


