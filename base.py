import json
import parser as parser
from math import sqrt

class Base:
    def __init__(self, filename):
        self.fichier = filename
        self.cases = parser.Parser(filename).get_cases()

    def calcul_proximite(self, cible):
        resultat = {}
        for i in range(len(self.cases)):
            poids = 0
            chiffre = 0
            for des in self.cases[i].descripteurs:
                descripteur = cible.get_descripteur(des['nom_desc'])
                if descripteur['poids'] == -1:
                    if descripteur['valeur'] != des['valeur']:
                        chiffre = 0
                        break
                    else:
                        chiffre += 1
                elif descripteur['valeur'] == des['valeur']:
                    chiffre += 1 * descripteur['poids']
                    poids += descripteur['poids']
                else:
                    if isinstance((descripteur['valeur']),str):
                        if des['nom_desc'] == "meublage":
                            if descripteur['valeur'] == "bien_meuble":
                                a_diff = 3
                            elif descripteur['valeur'] == "peu_meuble":
                                a_diff = 2
                            elif descripteur['valeur'] == "non_meuble":
                                a_diff = 1

                            if des['valeur'] == "bien_meuble":
                                differe = 3
                            elif des['valeur'] == "peu_meuble":
                                differe = 2
                            elif des['valeur'] == "non_meuble":
                                differe = 1
                        elif des['nom_desc'] == "proprete":
                            if descripteur['valeur'] == "tres_bon":
                                a_diff = 4
                            elif descripteur['valeur'] == "bon":
                                a_diff = 3
                            elif descripteur['valeur'] == "moyen":
                                a_diff = 2
                            elif descripteur['valeur'] == "mauvais":
                                a_diff = 1

                            if des['valeur'] == "tres_bon":
                                differe = 4
                            elif des['valeur'] == "bon":
                                differe = 3
                            elif des['valeur'] == "moyen":
                                differe = 2
                            elif des['valeur'] == "mauvais":
                                differe = 1
                        chiffre += sqrt((a_diff - differe) ** 2) * descripteur['poids']
                        poids += descripteur['poids']
                    else : 
                        chiffre += sqrt((descripteur['valeur'] - des['valeur']) ** 2) * descripteur['poids']
                        poids += descripteur['poids']
            if poids != 0:
                chiffre /= poids
            if chiffre != 0:
                chiffre = (1 / chiffre)
            resultat[i] = chiffre

        return resultat
    
    def get(self, i):
        return self.cases[i]

    def ajout(self, c):
        c.enleve_poids()
        self.cases.append(c)
        self.sauvegarde()

    def sauvegarde(self):
        resultat = []

        for c in self.cases:
            tempo = {
                "descripteurs": c.descripteurs,
                "solution": c.solution
            }
            resultat.append(tempo)

        with open(self.fichier, 'w+') as file:
            json.dump(resultat, file, indent='\t')

    def affiche(self):
        for cases in self.cases:
            print(f"{cases.descripteurs}, {cases.solution}")

