class Cas:
    def __init__(self):
        self.descripteurs = []
        self.solution = None

    def get_descripteur(self, nom):
        for des in self.descripteurs:
            if des['nom_desc'] == nom:
                return des

    def add_solution(self, sol):
        self.solution = sol

    def enleve_poids(self):
        for descr in self.descripteurs:
            descr.pop('poids')

    def add_descripteur(self, d):
        assert isinstance(d, dict)
        self.descripteurs.append(d)

    def __repr__(self) -> str:
        resultat = "Descripteurs :\n"
        for d in self.descripteurs:
            resultat += f"\t{d['nom_desc']}: {d['valeur']}\n"
        resultat += f"Prix : {'Inconnu' if self.solution == None or 0 else self.solution}\n"
        return resultat

