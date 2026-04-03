class AucuneNotesException(Exception):
       pass
class Etudiant:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom= prenom
        self.notes= []
    def ajouter_notes(self,note):
        self.notes.append(note)
    def moyenne(self):
        if len(self.notes)==0:
          raise AucuneNotesException("Impossible de calculer la moyenne: aucune note enregistree")
        else:
             return sum(self.notes)/len(self.notes)

class Promotion:
    def __init__(self,nom_promotion):
        self.nom_promotion = nom_promotion
        self.etudiants= []
    def ajouter_etudiants(self, etudiant):
        self.etudiants.append(etudiant)
    def meilleur_etudiant(self):
        return max(self.etudiants, key= lambda e: e.moyenne())
    def afficher_classement (self):
        classement= sorted(self.etudiants, key= lambda e: e.moyenne(), reverse= True)
        for e in classement:
            print(e.nom, e.prenom,"moyenne:", e.moyenne())

class Etudiant_boursier(Etudiant):
     def __init__(self, nom, prenom, montant_bourses):
         super().__init__(nom, prenom)
         self.montant_bourses = montant_bourses
     def afficher_profil(self):
         print("nom", self.nom, self.prenom)
         print("moyenne", self.moyenne())
         print("bourse", self.montant_bourses)




if __name__ == "__main__":
    promo = Promotion("2025")

    e1=Etudiant("Anthony", "Parker")
    e2= Etudiant("Erika", "De_la_vegas")
    e3= Etudiant_boursier("charlies", "apha", 1200)
    e4= Etudiant("jumior", "morgan")

    e1.ajouter_notes(13)
    e2.ajouter_notes(16)
    e3.ajouter_notes(17)
    e4.ajouter_notes(18)

    e1.ajouter_notes(12)
    e2.ajouter_notes(11)
    e3.ajouter_notes(10)
    e4.ajouter_notes(18)


    e1.ajouter_notes(6)
    e2.ajouter_notes(10)
    e3.ajouter_notes(4)
    e4.ajouter_notes(18)

    promo.ajouter_etudiants(e1)
    promo.ajouter_etudiants(e2)
    promo.ajouter_etudiants(e3)

    print("classement :")
    promo.afficher_classement()
    print (" profil du boursier")
    e3.afficher_profil()

    e5 = Etudiant("test", "vide")

    try:
        print(e5.moyenne())
    except AucuneNotesException as e:
        print (" erreur: ", e)









