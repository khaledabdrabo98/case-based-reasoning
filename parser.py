import json
import cas as c

class Parser:
    def __init__(self, file):
        self.cases = []
        doc = None

        with open(file, 'r') as f:
            doc = json.load(f)

        if doc != None:
            for ligne in doc:
                tmp = c.Cas()
                tmp.add_solution(ligne['solution'])
                for desc in ligne['descripteurs']:
                    tmp.add_descripteur(desc)
                self.cases.append(tmp)

    def get_cases(self):
        return self.cases
