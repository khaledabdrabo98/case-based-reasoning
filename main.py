# TP DynCo 2022
# RaPC
#ABDRABO Khaled
#BRIGNONE Jean


#############################################
#                                           #
# POUR CHANGER LE CAS TEST, ALLER LIGNE 163 #
#                                           #
#############################################



"""
Aperçu du cycle de raisonnement
• Élaboration : construire un cas cible et le préparer en fonction de
l’objectif du raisonnement
• Remémoration : rechercher dans la base de cas un cas source
similaire dont la solution a des chances de servir de solution pour le
problème cible
• Réutilisation : adaptation de la solution du cas source pour tenir
compte des différences avec le problème cible
• Révision : corriger la solution si elle ne donne pas satisfaction
• Apprentissage : mémoriser le cas nouvellement résolu pour une
réutilisation future éventuelle.
"""
#import pandas as pd
from random import choice
from base import Base
from cas import Cas

##### FILE OPENING / READING #####
# file = open("base.csv")
# #print(type(file))

# csvreader = csv.reader(file)
# header = []
# header = next(csvreader)
# print(header)

# descripteurs = []
# for desc in csvreader:
#         descripteurs.append(desc)
# print(descripteurs)


##### CYCLE DE RAISONNEMENT#####

def elaboration(descripteurs):
    c = Cas()
    for des in descripteurs:
        c.add_descripteur(des)
    return c

def rememoration(base, cas):
    prox = base.calcul_proximite(cas)
    resultat = []
    m = max(prox.values())

    if m == 0:
        return -1
    else:
        for k, v in prox.items():
            if v == m:
                resultat.append(k)
        return base.get(choice(resultat))

def reutilisation(source, appart_cible):
    solution = source.solution
    difference = 0
    for descr in source.descripteurs:
        d = appart_cible.get_descripteur(descr['nom_desc'])
        if isinstance((d['valeur']),str):
            if descr['nom_desc'] == "meublage":
                if d['valeur'] == "bien_meuble":
                    a_diff = 3
                elif d['valeur'] == "peu_meuble":
                    a_diff = 2
                elif d['valeur'] == "non_meuble":
                    a_diff = 1

                if descr['valeur'] == "bien_meuble":
                    differe = 3
                elif descr['valeur'] == "peu_meuble":
                    differe = 2
                elif descr['valeur'] == "non_meuble":
                    differe = 1
            elif descr['nom_desc'] == "proprete":
                if d['valeur'] == "tres_bon":
                    a_diff = 4
                elif d['valeur'] == "bon":
                    a_diff = 3
                elif d['valeur'] == "moyen":
                    a_diff = 2
                elif d['valeur'] == "mauvais":
                    a_diff = 1

                if descr['valeur'] == "tres_bon":
                    differe = 4
                elif descr['valeur'] == "bon":
                    differe = 3
                elif descr['valeur'] == "moyen":
                    differe = 2
                elif descr['valeur'] == "mauvais":
                    differe = 1
            difference2 = a_diff - differe
        else : 
            difference2 = d['valeur'] - descr['valeur']

        if d['nom_desc'] == "surface":
            difference += difference2 * 2.5
        elif d['nom_desc'] == "pieces":
            difference += difference2 * 25
        elif d['nom_desc'] == "DPE":
            difference += difference2 * 10
        elif (d['nom_desc'] == "ascenseur"):
            if difference2 == -1:
                difference -= 60
            elif difference2 == 1:
                difference += 60
        elif d['nom_desc'] == "meublage":
            if d['valeur'] == "bien_meuble":
                difference += 80
            elif d['valeur'] == "peu_meuble":
                difference += 40
            elif d['valeur'] == "non_meuble":
                difference += 0
        elif d['nom_desc'] == "proprete":
            if d['valeur'] == "tres_bon":
                difference += 60
            elif d['valeur'] == "bon":
                difference += 40
            elif d['valeur'] == "moyen":
                difference += 20
            elif d['valeur'] == "mauvais":
                difference += 0
    solution += difference
    appart_cible.solution = solution

def revision(base, case):
    verification = False
    reponse_entree  = 0.

    while not verification:
        try:
            reponse_entree = float(input("Prix : "))
            verification = True
        except ValueError:
            verification = False
            print("Veuillez entrer un nombre.")

    case.solution = reponse_entree
    base.ajout(case)
    print("Le cas entré a été ajouté à la base.")

def confirmation(base, case):
    print(f"Je propose {case.solution} comme nouveau prix, si cela vous contient entrez 'OUI', sinon, entrez 'NON' (veuillez resepcter la casse)")
    resp = input("[OUI/NON] : ")

    if resp == 'OUI':
        base.ajout(case)
        print("Le cas entré a été ajouté à la base.")
    elif resp == 'NON':
        print("Veuillez proposer un prix qui vous conviendrait mieux.")
        revision(base, case)


def main():
    b = Base('base.json')
    ###### POUR CHANGER LE CAS TEST CHANGER ICI #######
    descripteurs = [
        {
            "nom_desc": "surface",
            "valeur": 55,
            "poids": 1
        },
        {
            "nom_desc": "pieces",
            "valeur": 4,
            "poids": 1
        },
        {
            "nom_desc": "ascenseur",
            "valeur": 0,
            "poids": -1
        },
        {
            "nom_desc": "DPE",
            "valeur": 3,
            "poids": 1
        },
        {
            "nom_desc": "meublage",
            "valeur": "peu_meuble",
            "poids": 1
        },
        {
            "nom_desc": "proprete",
            "valeur": "moyen",
            "poids": 1
        },
    ]

    c = elaboration(descripteurs)
    case = rememoration(b, c)

    print(f"Voici le cas entré :")
    print(c)

    if case == -1:
        print("Impossible de trouver une ressemblance avec un cas de la base. Veuillez proposer vous-même un prix.")
        revision(b, c)
    else:
        print("Voici le cas qui a la meilleure proximité :")
        print(case)
        reutilisation(case, c)
        confirmation(b, c)

if __name__ == '__main__':
    main()
