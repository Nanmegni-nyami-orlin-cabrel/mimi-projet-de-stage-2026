from datetime import datetime
import json
import os


class Tache:
    # On ne demande que ce qui est variable à la création
    def __init__(self, titre, description, statut="en cours", date_creation=None):
        self.titre = titre
        self.description = description
        self.statut = statut
        # Si aucune date n'est fournie (nouvelle tâche), on prend l'heure actuelle
        self.date_creation = date_creation if date_creation else datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def terminer(self):
        self.statut = "terminée"

    def afficher(self):
        print(f"[{self.statut}] {self.titre} (Créée le {self.date_creation})")
        print(f"    Description : {self.description}")


class Gestionnaire:
    def __init__(self):
        self.liste_taches = []
        self.charger_depuis_json()  # Chargement auto au démarrage

    def ajouter_tache(self, titre, description):
        nouvelle_tache = Tache(titre, description)
        self.liste_taches.append(nouvelle_tache)
        self.sauvegarder()

    def terminer_tache(self, titre):
        for tache in self.liste_taches:
            if tache.titre == titre:
                tache.terminer()
                self.sauvegarder()
                break

    def supprimer_tache(self, titre):
        # On recrée la liste en excluant celle qui a ce titre
        self.liste_taches = [t for t in self.liste_taches if t.titre != titre]
        self.sauvegarder()

    def afficher_toutes(self):
        print("\n--- TOUTES LES TÂCHES ---")
        for tache in self.liste_taches:
            tache.afficher()

    def afficher_en_cours(self):
        print("\n--- TÂCHES EN COURS ---")
        for tache in self.liste_taches:
            if tache.statut == "en cours":
                tache.afficher()

    def sauvegarder(self):
        # On transforme les objets en dictionnaires pour JSON
        data = [t.__dict__ for t in self.liste_taches]
        with open("taches.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def charger_depuis_json(self):
        if os.path.exists("taches.json"):
            with open("taches.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                # On reconstruit les objets Tache
                self.liste_taches = [Tache(**d) for d in data]


if __name__ == "__main__":
    gest = Gestionnaire()

    # Test : On ajoute seulement si la liste est vide (évite les doublons au redémarrage)
    if not gest.liste_taches:
        gest.ajouter_tache("Laver les habits", "Laver avec de l'eau et du savon")
        gest.ajouter_tache("Nettoyer le sol", "Salon, cuisine et douche")
        gest.ajouter_tache("Laver la vaisselle", "Plats, verres et fourchettes")

        gest.terminer_tache("Laver les habits")
        gest.supprimer_tache("Laver la vaisselle")

    gest.afficher_toutes()
    gest.afficher_en_cours()